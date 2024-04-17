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

