class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rRes = sum(nums)
        lRes = 0
        for index,val in enumerate(nums):
            rRes -= val
            # print(lRes,rRes)
            if rRes == lRes:
                return index
            lRes += val
        return -1

if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    result = Solution().pivotIndex(nums)
    print(result)