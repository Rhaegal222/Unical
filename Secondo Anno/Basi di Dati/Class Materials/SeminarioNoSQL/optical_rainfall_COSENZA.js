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
       $match: {"data.description": {$in: ['Optical rainfall'
                                             ] } }
    },
     {
      $addFields: {

          rainfallIndex: {$switch: {
                           branches: [
                              { case: 
                                  { $in: [ 'Optical rainfall', "$data.description"]                                      
                                  }, 
                                  then: {$indexOfArray: [ "$data.description", 'Optical rainfall']} 
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
        "Optical rainfall (mm)": {$toDouble : {$arrayElemAt: ["$data.value", '$rainfallIndex']} }, 
        "date": {
          "$dateFromString": {
            "dateString": "$timestamp"
          }
        }
      }
    },
          

])

