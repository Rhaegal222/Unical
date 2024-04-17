#pragma once
#include "../Command/Command.h"

class Mediator {
public:
    virtual ~Mediator() = default;
    virtual void executeCommand(Command* command) = 0;
};
