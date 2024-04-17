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
       $match: {"data.description": {$in: ['Noise', 'PM10'
                                             ] } }
    },
     {
      $addFields: {
          timestamp_date : {$toDate : {
                              "$dateFromString": {
                                "dateString": "$timestamp",
                                "timezone": "Europe/Rome"
                              } }
          },

          NoiseIndex: {$switch: {
                           branches: [
                              { case: 
                                  { $in: [ 'Noise', ', "$data.description"]                                      
                                  }, 
                                  then: {$indexOfArray: [ "$data.description", 'Noise']} 
                              }
                           ],
                           default: -1
                          }  
                         } ,
        TemperatureIndex: {$switch: {
                           branches: [
                              { case: 
                                  { $in: [ 'Temperature', "$data.description"]                                      
                                  }, 
                                  then: {$indexOfArray: [ "$data.description", 'Temperature']} 
                              }
                           ],
                           default: -1
                          }  
                         } 
      }
     },
     {
        $group: {
            _id: {
                year: { $year: '$timestamp_date'},
                month: { $month: "$timestamp_date" },
                day: { $dayOfMonth: "$timestamp_date" },
                hour: { $hour: "$timestamp_date"},
                interval: {
                    "$subtract": [ 
                      { "$minute": "$timestamp_date" },
                      { "$mod": [{ "$minute": "$timestamp_date"}, 15] }
                    ]
                  }
            },
            "date": { $first:'$timestamp_date'},
            "Media_Noise": { $avg: {$toDouble : {$arrayElemAt: ["$data.value", '$NoiseIndex']} }},
            "Media_Temperature": { $avg: {$toDouble : {$arrayElemAt: ["$data.value", '$TemperatureIndex']} }},
        },  
     } ,                         
     {
      $project:
      {
        _id:0,
       "Noise (15 minuti)": "$Media_Noise" , 
       "PM 10 (μg/m^3) (15 minuti)":  "$Media_Temperature" ,                           
        "date": '$date'
      }
    },
          

])

