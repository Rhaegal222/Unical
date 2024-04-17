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

