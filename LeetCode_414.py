class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        a,b,c= float("-inf"),float("-inf"),float("-inf")
        for i in nums:
            if i > a:
                a,b,c = i,a,b
            elif i>b and i !=a:
                b,c = i,b
            elif i>c and i !=b and i !=a:
                c = i
        print(a,b,c)
        return c if c != float("-inf") else a

if __name__ == '__main__':
    nums = [2, 2, 3, 1]
    nums = [1,1,2]
    result = Solution().thirdMax(nums)
    print(result)


