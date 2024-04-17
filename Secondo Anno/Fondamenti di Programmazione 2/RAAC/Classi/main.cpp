#include "Car.h"
#include "Owner.h"
#include "VM.h"

#include <iostream>

using namespace std;

int	main()
{   
    VM db1;

    Owner Lucia(001, "Lucia", "Zero");
    Owner Amara(002, "Amara", "Vita");
    Owner Mia(003, "Mia", "Amara");
    Owner Anna(004, "Anna", "Camilla");

    Car Mini("MPV", "Mini", "W168", "AA000AA");
    Car Audi("Coupé", "Audi", "TT", "AA001AA");
    Car BMW("Spyder", "BMW", "Z4", "AA002AA");
    Car Opel("Sedan", "Opel", "Astra", "AA003AA");

    db1.addVehicle(&Mia, &Mini);  
    db1.addVehicle(&Lucia, &Audi);
    db1.addVehicle(&Amara, &BMW);
    db1.addVehicle(&Anna, &Opel);

    db1.printAllVehicles();

    return 0;
}
