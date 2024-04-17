#pragma once
#include "Observer/Observer.h"
#include "Strategy/Strategy.h"
#include <memory>

class Trader : public Observer {
    std::unique_ptr<TradingStrategy> strategy;
public:
    Trader(std::unique_ptr<TradingStrategy> strat);
    void update(float price) override;
};
