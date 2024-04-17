#include "Trader.h"

Trader::Trader(std::unique_ptr<TradingStrategy> strat) : strategy(std::move(strat)) {}

void Trader::update(float price) {
    strategy->execute(price);
}
