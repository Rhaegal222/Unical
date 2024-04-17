#include "Trader.cpp"
#include "Strategy/ConcreteStrategies.cpp"
#include "Observer/StockMarket.cpp"

int main() {
    StockMarket market;
    Trader aggressiveTrader(std::make_unique<AggressiveStrategy>());
    Trader conservativeTrader(std::make_unique<ConservativeStrategy>());

    market.attach(&aggressiveTrader);
    market.attach(&conservativeTrader);

    market.setPrice(100.0f); // This will notify all traders

    return 0;
}
