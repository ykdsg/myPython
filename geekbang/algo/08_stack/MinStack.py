class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.max = 100
        self.n = 0

    def push(self, val: int) -> None:
        if self.n >= self.max:
            return None
        self.items.append(val)
        self.n += 1

    def pop(self) -> None:
        if self.n == 0:
            return
        self.n -= 1

    def top(self) -> int:
        if self.n == 0:
            return None
        self.n -= 1
        cur = self.items[self.n]
        return cur

    def getMin(self) -> int:
        min = self.items[0]
        for i in range(0, self.n):
            if min > self.items[i]:
                min = self.items[i]
        return min


if __name__ == '__main__':
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(-1)
    param_4 = obj.getMin()
    print(param_4)
    obj.pop()
    param_3 = obj.top()
    print(param_3)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
