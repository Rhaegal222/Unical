db.getCollection("collection1").aggregate([
    //COMUNE DI COSENZA
    // A partire dal 03/01/2023  
    {
       $match: {"timestamp": {$gte: "2023-01-03"}}
    },
    // Sensore del comune di Cosenza
    {
       $match: {"name": {$in: ['Weather Station Cosenza01'] } }
    },

    //Misurazioni interessate
     {
       $match: {"data.description": {$in: ['Noise'
                                             ] } }
    },
     {
      $addFields: {

          noiseIndex: {$switch: {
                           branches: [
                              { case: 
                                  { $in: [ 'Noise', "$data.description"]                                      
                                  }, 
                                  then: {$indexOfArray: [ "$data.description", 'Noise']} 
                              }
                           ],
                           default: -1
                          }  
                         } ,        
      }
     },
     {
      $project:
      {
        //"data": 1,
        "_id": 0,
        "Rumore (db)": {$toDouble : {$arrayElemAt: ["$data.value", '$noiseIndex']} }, 
        "date": {
          "$dateFromString": {
            "dateString": "$timestamp"
          }
        }
      }
    },
          

])

