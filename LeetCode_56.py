class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lList,rList = [],[]
        for i in intervals:
            lList.append(i[0])
            rList.append(i[1])
        lList.sort(reverse=True)
        rList.sort(reverse=True)
        stack = []
        resList = []
        #用栈来保存左边界，一旦出现右边界比左边界高，就退栈，为0就出一个输出结果
        while len(lList) !=0 or len(rList) != 0:
            # print(lList,rList,stack,resList)
            if lList and len(stack) == 0:
                pop = lList.pop()
                stack.append(pop)
            else:
                if lList and rList:
                    if lList[-1]<= rList[-1]:
                        stack.append(lList.pop())
                    else:
                        lastL = stack.pop()
                        lastR = rList.pop()
                        if len(stack) == 0:
                            resList.append([lastL,lastR])
                elif len(rList) != 0:
                    lastL = stack.pop()
                    lastR = rList.pop()
                    if len(stack) == 0:
                        resList.append([lastL, lastR])
        return resList

if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = Solution().merge(intervals)
    print(result)