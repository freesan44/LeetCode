class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start+i*2)
        print(nums)
        ret = start
        for j in range(1, n):
            ret = ret^nums[j]
        return ret
if __name__ == '__main__':
    n = 5
    start = 0
    ret = Solution().xorOperation(n, start)
    print(ret)