#pragma once
#include "Command.h"
#include <iostream>

class LightOnCommand : public Command {
public:
    void execute() override;
};

class ThermostatSetCommand : public Command {
public:
    void execute() override;
};
