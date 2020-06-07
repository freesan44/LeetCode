class Solution:
    def shuffle(self, nums: [int], n: int) -> [int]:
        tempList = []
        for i in range(n):
            tempList.append(nums[i])
            tempList.append(nums[i+n])
        return tempList


if __name__ == '__main__':
    # nums = [2,5,1,3,4,7]
    # n = 3
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    ret = Solution().shuffle(nums, n)
    print(ret)