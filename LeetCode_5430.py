class BrowserHistory:
    historyList = []
    curIndex = -1
    def __init__(self, homepage: str):
        self.historyList.clear()
        self.curIndex = -1
        self.historyList.append(homepage)


    def visit(self, url: str) -> None:
        # print(self.historyList)
        # print(self.curIndex)
        # print(self.historyList[:None if self.curIndex+1 == 0 else self.curIndex+1])
        self.historyList = self.historyList[:None if self.curIndex+1 == 0 else self.curIndex+1]
        self.historyList.append(url)
        self.curIndex = -1


    def back(self, steps: int) -> str:
        self.curIndex += -steps
        # print("back"+str(steps))
        # print(self.curIndex)
        # print(self.historyList)
        if abs(self.curIndex) > len(self.historyList):
            self.curIndex = -len(self.historyList)
        return self.historyList[self.curIndex]


    def forward(self, steps: int) -> str:
        self.curIndex += steps
        if self.curIndex > -1:
            self.curIndex = -1#回到最新一页
        return self.historyList[self.curIndex]


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
param_2 = obj.back(1)
print(param_2)
param_2 = obj.back(1)
print(param_2)
param_3 = obj.forward(1)
print(param_3)
obj.visit("linkedin.com")
param_3 = obj.forward(2)
print(param_3)
param_2 = obj.back(4)
print(param_2)
param_2 = obj.back(7)
print(param_2)
obj.visit("yoyo.com")
param_2 = obj.back(4)
print(param_2)
param_3 = obj.forward(10)
print(param_3)
param_2 = obj.back(8)
print(param_2)
param_3 = obj.forward(5)
print(param_3)