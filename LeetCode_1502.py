class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # 先进行排序，然后通过错位zip压缩成一个等差元组（假如成立的情况下）
        arr.sort()
        zipList = list(zip(arr,arr[1:]))
        # print(zipList)
        resDict = dict()#用字典方式存取比较快速
        for x,y in zipList:
            resDict[x-y] = 1
        # print(resDict)
        return len(resDict) == 1#如果为等差，字典只有一个值



if __name__ == '__main__':
    arr = [3,5,1]
    ret = Solution().canMakeArithmeticProgression(arr)
    print(ret)