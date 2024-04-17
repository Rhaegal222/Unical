#include "ConcreteCommands.h"

void LightOnCommand::execute() {
    std::cout << "Turning on the light." << std::endl;
}

void ThermostatSetCommand::execute() {
    std::cout << "Setting the thermostat." << std::endl;
}
