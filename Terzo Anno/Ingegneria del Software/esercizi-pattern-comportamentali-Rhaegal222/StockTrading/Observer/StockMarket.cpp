#include "StockMarket.h"

void StockMarket::attach(Observer* observer) {
    observers.push_back(observer);
}

void StockMarket::setPrice(float price) {
    stockPrice = price;
    notify();
}

void StockMarket::notify() {
    for (Observer* observer : observers) {
        observer->update(stockPrice);
    }
}
