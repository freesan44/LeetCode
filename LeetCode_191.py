class Solution:
    def hammingWeight(self, n: int) -> int:
        strI = bin(n)#转成二进制
        # print(n,strI)
        return strI.count("1")

if __name__ == '__main__':
    nums = 11111111111111111111111111111101
    result = Solution().hammingWeight(nums)
    print(result)