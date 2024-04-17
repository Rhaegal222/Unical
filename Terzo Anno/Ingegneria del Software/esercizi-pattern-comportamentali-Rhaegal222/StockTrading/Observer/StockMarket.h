#pragma once

#include <vector>
#include "Observer.h"

class StockMarket {
    float stockPrice;
    std::vector<Observer*> observers;
public:
    void attach(Observer* observer);
    void setPrice(float price);
    void notify();
};