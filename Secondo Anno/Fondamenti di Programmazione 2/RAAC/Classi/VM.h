#ifndef __VM__H__
#define __VM__H__

#include "Vehicle.h"
#include "Car.h"
#include "Owner.h"

#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class VM{
private:
    unordered_map<Owner*, Vehicle*> vehicleManager;
public:

    //Aggiungi Veicolo
    void addVehicle(Owner* own, Vehicle* veh){
        unordered_map<Owner*, Vehicle*>::iterator it;
        if(vehicleManager.empty())
            vehicleManager.insert({own, veh});
        else{
            for(it=vehicleManager.begin(); it!=vehicleManager.end();it++){
                auto owner = (*it).first;
                cout << own->get_id() << " " << owner->get_id() << endl;
                if(own->get_id() < owner->get_id())
                    vehicleManager.insert(it++, {own, veh});
            }
        }
    }

    //Rimuovi Veicolo
    void printAllAddress(){
        unordered_map<Owner*, Vehicle*>::iterator it;
        for(it=vehicleManager.begin(); it!=vehicleManager.end();it++){
            auto owner = (*it).first;
            cout << owner << endl;
        }
    }

    /*StampaTutti*/
    void printAllVehicles(){
        cout<<vehicleManager.size()<<" veicoli memorizzati"<<endl;

        cout<<"ID"<<"\t"<<"Nome"<<"\t"<<"Cognome"<<"\t"<<"Tipo"<<"\t"<<"Marca"<<"\t"<<"Modello"<<endl;

        unordered_map<Owner*, Vehicle*>::iterator it;
        for(it=vehicleManager.begin(); it!=vehicleManager.end();it++){
            auto owner = (*it).first;
            auto vehicle = (*it).second;
            cout << *owner << *vehicle << endl;
        }
    }
    
};

#endif  //!__VM__H__