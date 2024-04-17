#ifndef __CONCRETEDECORATORS__H__
#define __CONCRETEDECORATORS__H__

#include "DishDecorator.h"

// Un decoratore concreto, ad esempio aggiunta di formaggio extra.
class ExtraCheeseDecorator : public DishDecorator {
public:
    ExtraCheeseDecorator(Dish* dish) : DishDecorator(dish) {}

    std::string getDescription() override {
        return decoratedDish->getDescription() + " con extra formaggio";
    }
};

// Un decoratore concreto, ad esempio aggiunta di funghi.
class MushroomsDecorator : public DishDecorator {
public:
    MushroomsDecorator(Dish* dish) : DishDecorator(dish) {}

    std::string getDescription() override {
        return decoratedDish->getDescription() + " con funghi";
    }
};

#endif  //!__CONCRETEDECORATORS__H__
