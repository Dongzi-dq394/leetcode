class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.Min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.Min:
            self.Min.append(x)
        else:
            self.Min.append(min(x, self.Min[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.Min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()