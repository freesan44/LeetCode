class Solution:
    def singleNumber(self, nums: [int]) -> int:
        #列表方式
        # tempList = []
        # for i in nums:
        #     if i in tempList:
        #         tempList.remove(i)
        #     else:
        #         tempList.append(i)
        # return tempList.pop()
        #字典方式
        # tempDic = {}
        # for i in nums:
        #     if i in tempDic:
        #         del tempDic[i]
        #     else:
        #         tempDic[i] = 1
        # return tempDic.popitem()[0]
        #异或
        ans = 0
        for i in nums:
            ans ^= i
        return ans

if __name__ == '__main__':
    nums = [1,2,3,2,1]
    result = Solution().singleNumber(nums)
    print(result)