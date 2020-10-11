class MaxStack:
    
    # Solution from Solution: Two Stacks (160ms: 70.91%)

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.max_num = []

    def push(self, x: int) -> None:
        self.arr.append(x)
        if not self.max_num:
            self.max_num.append(x)
        else:
            self.max_num.append(max(x, self.max_num[-1]))

    def pop(self) -> int:
        self.max_num.pop()
        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def peekMax(self) -> int:
        return self.max_num[-1]

    def popMax(self) -> int:
        temp = []
        MAX = self.max_num[-1]
        while self.arr[-1]!=MAX:
            temp.append(self.arr.pop())
            self.max_num.pop()
        self.arr.pop()
        self.max_num.pop()
        for item in temp[::-1]:
            self.arr.append(item)
            if not self.max_num:
                self.max_num.append(item)
            else:
                self.max_num.append(max(item, self.max_num[-1]))
        return MAX
        
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()