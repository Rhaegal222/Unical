#include "Bridge/ConcreteCuisines.h"
#include "Decorator/ConcreteDecorators.h"
#include "Decorator/ConcreteDish.h"

#include <string>
#include <iostream>

using namespace std;

int main() {
    // Utilizzo del Bridge Pattern per descrivere due diversi tipi di cucina.
    CuisineType* italianCuisine = new ItalianCuisine();
    CuisineType* japaneseCuisine = new JapaneseCuisine();

    cout << "Cucina italiana: " << italianCuisine->describeCuisine() << endl;
    cout << "Cucina giapponese: " << japaneseCuisine->describeCuisine() << endl;

    // Creazione e decorazione di un piatto italiano
    cout << "Sto preparando un piatto italiano..." << endl;
    Dish* myItalianDish = new Pizza();
    cout << "Ho preparato una " << myItalianDish->getDescription() << endl;
    Dish* decoratedItalianDish = new ExtraCheeseDecorator(myItalianDish);
    cout << "Il piatto è pronto: " << decoratedItalianDish->getDescription() << endl << endl;

    // Decorazione di un piatto italiano già esistente
    cout << "Sto decorando il piatto italiano..." << endl;
    decoratedItalianDish = new MushroomsDecorator(decoratedItalianDish);
    cout << "Il piatto è pronto: " << decoratedItalianDish->getDescription() << endl << endl;

    // Creazione e decorazione di un piatto giapponese (esempio: Sushi).
    cout << "Sto prepando un piatto giapponese..." << endl;
    Dish* myJapaneseDish = new Sushi();
    cout << "Ho preparato del " << myJapaneseDish->getDescription() << endl;
    Dish* decoratedJapaneseDish = new MushroomsDecorator(myJapaneseDish);
    cout << "Il piatto è pronto: " << decoratedJapaneseDish->getDescription() << endl << endl;
    

    delete italianCuisine;
    delete japaneseCuisine;
    delete decoratedItalianDish;

    return 0;
}
