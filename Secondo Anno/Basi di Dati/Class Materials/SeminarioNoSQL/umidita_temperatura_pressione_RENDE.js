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
       $match: {"data.description": {$in: ['Humidity', 'Temperature', 'Atmospheric pressure'
                                             ] } }
    },
     {
      $addFields: {
          //Prendi l'umidità
          humidityIndex: {$switch: {
                           branches: [
                              { case: 
                                  { $in: [ 'Humidity', "$data.description"]                                      
                                  }, 
                                  then: {$indexOfArray: [ "$data.description", 'Humidity']} 
                              }
                           ],
                           default: -1
                          }  
                         } ,
        temperatureIndex: {$switch: {
                           branches: [
                              { case: 
                                  { $in: [ 'Temperature', "$data.description"]                                      
                                  }, 
                                  then: {$indexOfArray: [ "$data.description", 'Temperature']} 
                              }
                           ],
                           default: -1
                          }  
                         } ,
        atmosphericPressureIndex: {$switch: {
                           branches: [
                              { case: 
                                  { $in: [ 'Atmospheric pressure', "$data.description"]                                      
                                  }, 
                                  then: {$indexOfArray: [ "$data.description", 'Atmospheric pressure']} 
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
        "Umidità (%)": {$toDouble : {$arrayElemAt: ["$data.value", '$humidityIndex']} }, 
        "Temperatura (°C)": {$toDouble : {$arrayElemAt: ["$data.value", '$temperatureIndex']} }, 
        "Pressione Atmosferica (Kpa)": {$toDouble : {$arrayElemAt: ["$data.value", '$atmosphericPressureIndex']} }, 
        "date": {
          "$dateFromString": {
            "dateString": "$timestamp"
          }
        }
      }
    },
          

])

