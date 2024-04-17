#pragma once

class Observer {
public:
    virtual ~Observer() = default;
    virtual void update(float price) = 0;
};
