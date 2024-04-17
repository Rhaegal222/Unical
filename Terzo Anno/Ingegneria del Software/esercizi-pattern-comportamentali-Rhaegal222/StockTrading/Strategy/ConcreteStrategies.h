#pragma once
#include "Strategy.h"
#include <iostream>

class AggressiveStrategy : public TradingStrategy {
public:
    void execute(float price) override;
};

class ConservativeStrategy : public TradingStrategy {
public:
    void execute(float price) override;
};
