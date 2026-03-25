class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    s.push(3)
    s.push(7)
    assert s.getMin() == 3
    assert s.top() == 7
    s.pop()
    assert s.getMin() == 3
    s.pop()
    assert s.getMin() == 5
    assert s.top() == 5
    print("All tests passed!")
