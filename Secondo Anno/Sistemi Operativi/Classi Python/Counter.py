class Counter:
    def getValue(self):
        return self._value

    def click(self):
        self._value += 1

    def reset(self):
        self._value = 0

def main():
    tally = Counter()
    tally.reset()
    
    for i in range(10): tally.click()

    result = tally.getValue()
    print('Value: ', result)

    tally.reset()

    for i in range(3): tally.click()
    result = tally.getValue()
    print('Value: ', result)

main()