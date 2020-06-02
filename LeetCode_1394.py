class Solution:
    def findLucky(self, arr: [int]) -> int:
        lastSum = [-1]
        arr.sort(reverse=True)
        for each in arr:
            print(each)
            print(lastSum)
            #如果当前数不等于最后一位，代表中断重新算
            if each != lastSum[-1]:
                #判断上一个组合是否为幸运数
                if len(lastSum) == lastSum[-1]:
                    return lastSum[-1]
                lastSum.clear()
            lastSum.append(each)
        #针对排序结束后最后一个判断
        return (lastSum[-1] if len(lastSum) == lastSum[-1] else -1)


if __name__ == '__main__':
    arr = [1,2,2,3,3,3]
    arr = [2,2,3,4]
    ret = Solution().findLucky(arr)
    print(ret)