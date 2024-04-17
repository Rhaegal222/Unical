#ifndef __CAR__H__
#define __CAR__H__

#include "Vehicle.h"
#include <string>

using namespace std;

class Car : public Vehicle{
    string plate;
    public:
        Car(string type, string brand, string model, string plate) : 
            Vehicle( type, brand, model),
            plate(plate){}

        string get_plate(){return plate;}

};

#endif  //!__CAR__H__
