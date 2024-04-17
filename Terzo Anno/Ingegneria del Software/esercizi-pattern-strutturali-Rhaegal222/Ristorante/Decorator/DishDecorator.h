#ifndef __DISHDECORATOR__H__
#define __DISHDECORATOR__H__

#include "Dish.h"

// Decoratore base per aggiungere personalizzazioni.
class DishDecorator : public Dish {
protected:
    Dish* decoratedDish;

public:
    DishDecorator(Dish* dish) : decoratedDish(dish) {}
    virtual ~DishDecorator() {
        delete decoratedDish;
    }
};

#endif  //!__DISHDECORATOR__H__
