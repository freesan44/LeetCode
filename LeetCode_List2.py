class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except:
                break
        return len(nums)

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    ret = Solution().removeElement(nums, val)
    print(ret)