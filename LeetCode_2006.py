class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        length = len(nums)
        res = 0
        for i in range(length):
            for j in range(i+1,length):
                if k == abs(nums[i]-nums[j]):
                    res += 1
        return res