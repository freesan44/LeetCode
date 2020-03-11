class MinStack:

    def __init__(self):
        self.list = []
        self.minIndex = 0
        """
        initialize your data structure here.
        """


    def push(self, x: int) -> None:
        self.list.append(x)
        if len(self.list) > 0 and x < self.list[self.minIndex]:
            self.minIndex = self.list.index(x)
            # print("change: " + str(self.minIndex) + str(x))


    def pop(self) -> None:
        popNum = self.list.pop()
        if self.minIndex == (len(self.list)):
            # print("change: " + str(self.minIndex))
            self.minIndex = 0 if len(self.list) <=0 else self.list.index(min(self.list))
        return popNum


    def top(self) -> int:
        return None if len(self.list) <= 0 else self.list[-1]

    def getMin(self) -> int:
        # print("getMin: " + str(self.minIndex))
        return None if len(self.list) <= 0 else self.list[self.minIndex]

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
    # obj = MinStack()
    # obj.push(3)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
    # print(param_3)
    # print(param_4)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()