#pragma once
#include "Mediator.h"

class HomeAutomationMediator : public Mediator {
public:
    void executeCommand(Command* command) override;
};
