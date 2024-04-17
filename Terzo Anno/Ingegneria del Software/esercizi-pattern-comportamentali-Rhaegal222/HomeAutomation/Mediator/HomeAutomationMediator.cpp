#include "HomeAutomationMediator.h"

void HomeAutomationMediator::executeCommand(Command* command) {
    command->execute();
}
