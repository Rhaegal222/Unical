#ifndef  VEHICLE_H
#define VEHICLE_H

#include "Owner.h"

#include <string>
#include <iostream>

using namespace std;

class Vehicle{
    protected:
        string type, brand, model;
    
    public:
        Vehicle(string type, string brand, string model) : 
            type(type), 
            brand(brand), 
            model(model){};

        Vehicle(const Vehicle& Vehicle){};

        string get_type(){return type;}
        string get_brand(){return brand;}
        string get_model(){return model;}  

        friend ostream& operator<<(ostream& o, const Vehicle& veh){
		o << veh.type << "\t" << veh.brand << "\t" << veh.model;
		return o;
	    }
};
#endif  //VEHICLE.H