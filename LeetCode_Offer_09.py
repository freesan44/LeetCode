class CQueue:
    def __init__(self):
        self.queueListOut = []
        self.queueListTemp = []
    def appendTail(self, value: int) -> None:
        self.queueListTemp.append(value)

    def deleteHead(self) -> int:
        if len(self.queueListOut) <= 0 and len(self.queueListTemp)<= 0: return -1
        if len(self.queueListOut) != 0:
            return self.queueListOut.pop()
        while len(self.queueListTemp) != 0:
            self.queueListOut.append(self.queueListTemp.pop())
        return self.queueListOut.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
if __name__ == '__main__':
    obj = CQueue()
    obj.appendTail(1)
    obj.appendTail(2)
    obj.appendTail(3)
    param_2 = obj.deleteHead()
    print(param_2)