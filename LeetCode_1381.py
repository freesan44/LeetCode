class CustomStack:
    maxSize = 0
    stack = []

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = list()


    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) >= k:
            for i in range(0,k):
                self.stack[i] += val
        else:
            for i in range(len(self.stack)):
                self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
