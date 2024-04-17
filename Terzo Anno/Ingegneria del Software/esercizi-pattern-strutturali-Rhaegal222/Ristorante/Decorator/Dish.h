#ifndef __DISH__H__
#define __DISH__H__

#include <string>

// Interfaccia base per i piatti.
class Dish {
public:
    virtual ~Dish() = default;
    virtual std::string getDescription() = 0;
};

#endif  //!__DISH__H__
