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
       $match: {"data.description": {$in: ['16-bit value of Lux value of 20W'
                                             ] } }
    },
     {
      $addFields: {

          luxIndex: {$switch: {
                           branches: [
                              { case: 
                                  { $in: [ '16-bit value of Lux value of 20W', "$data.description"]                                      
                                  }, 
                                  then: {$indexOfArray: [ "$data.description", '16-bit value of Lux value of 20W']} 
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
        "Intensità luminosa (lux)": {$toDouble : {$arrayElemAt: ["$data.value", '$luxIndex']} }, 
        "date": {
          "$dateFromString": {
            "dateString": "$timestamp"
          }
        }
      }
    },
          

])

