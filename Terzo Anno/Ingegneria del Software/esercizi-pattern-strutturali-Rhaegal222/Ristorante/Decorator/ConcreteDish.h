#ifndef __CONCRETEDISH__H__
#define __CONCRETEDISH__H__

#include "Dish.h"

// Implementazione concreta di un piatto base, ad esempio la Pizza.
class Pizza : public Dish {
public:
    std::string getDescription() override {
        return "Pizza";
    }
};

// Implementazione concreta di un piatto base, ad esempio la Pasta.
class Pasta : public Dish {
public:
    std::string getDescription() override {
        return "Pasta";
    }
};

// Implementazione concreta di un piatto base, ad esempio il Sushi.
class Sushi : public Dish {
public:
    std::string getDescription() override {
        return "Sushi";
    }
};

#endif  //!__CONCRETEDISH__H__
