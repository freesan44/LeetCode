class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l1 = [i for i in nums if i % 2 == 0]
        l2 = [i for i in nums if i % 2 != 0]
        # print(l1)
        # print(l2)
        resList = []
        for i in l1:
            resList.append(i)
            resList.append(l2.pop())
        return resList


if __name__ == '__main__':
    nums = [4,2,5,7]
    ret = Solution().sortArrayByParityII(nums)
    print(ret)