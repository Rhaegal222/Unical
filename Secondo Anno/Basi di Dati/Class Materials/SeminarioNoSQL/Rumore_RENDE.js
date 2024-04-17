db.getCollection("collection1").aggregate([
    //COMUNE DI RENDE
    // A partire dal 01/12/2022 
    {
       $match: {"timestamp": {$gte: "2022-12-01"}}
    },
    // Sensore del comune di Rende
    {
       $match: {"name": {$in: ['Weather Station Rende01'] } }
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

