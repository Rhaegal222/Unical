#pragma once

class TradingStrategy {
public:
    virtual ~TradingStrategy() = default;
    virtual void execute(float price) = 0;
};
