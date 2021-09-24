class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums).most_common()
        x,y = counter[-1]
        # print(x,y)
        return x



if __name__ == '__main__':
    # nums = [2,2,3,2]
    nums = [0, 1, 0, 1, 0, 1, 100]
    ret = Solution().singleNumber(nums)
    print(ret)