#include "Mediator/HomeAutomationMediator.cpp"
#include "Command/ConcreteCommands.cpp"

int main() {
    HomeAutomationMediator mediator;
    LightOnCommand lightOn;
    ThermostatSetCommand setThermostat;

    mediator.executeCommand(&lightOn);
    mediator.executeCommand(&setThermostat);

    return 0;
}
