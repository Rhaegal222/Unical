#include "ConcreteStrategies.h"

void AggressiveStrategy::execute(float price) {
    std::cout << "Executing aggressive strategy for price " << price << std::endl;
}

void ConservativeStrategy::execute(float price) {
    std::cout << "Executing conservative strategy for price " << price << std::endl;
}
