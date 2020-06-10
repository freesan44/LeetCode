class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        index = 0
        lenL = len(nums)
        while lenL!=0:
            index += 1
            if nums[index%lenL] == nums[(index*2)%lenL] and index%lenL != (index*2)%lenL:
                return nums[index%lenL]
            if index%lenL == (index*2)%lenL:
                lenL -= 1
        return 0

if __name__ == '__main__':
    numsList = [1,3,4,2,2]
    # numsList = [3,1,3,4,2]
    # numsList = [1,1,2]
    print(100<<1)
    # ret = Solution().findDuplicate(numsList)
    # print(ret)