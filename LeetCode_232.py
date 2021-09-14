class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Alist = []
        self.Blist = []
        self.peekIndex = None


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.Alist.append(x)
        if len(self.Alist)== 1:
            self.peekIndex = x


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #如果B为空，就从A倒到B再处理
        if len(self.Blist) == 0 and len(self.Alist) == 0:
            return None
        if len(self.Blist) != 0:
            return self.Blist.pop()
        else:
            while len(self.Alist)!=0:
                self.Blist.append(self.Alist.pop())
            self.peekIndex = None
            return self.Blist.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.Blist.__len__() == 0:
            return self.peekIndex
        else:
            return self.Blist[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.peekIndex == None and len(self.Blist) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()