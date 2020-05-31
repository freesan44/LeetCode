class Solution:
    def removeDuplicates(self, nums:[int]) -> int:
        lenDup = len(set(nums))#去重后的长度
        if len(nums) == 1: return 1
        i = 0
        while i < lenDup-1:
            print(nums[i])
            if nums[i] == nums[i+1]:
                temp = nums[i]
                print(nums[i+1:])
                # nums[i:-1] = nums[i+1:]
                nums[i+1: len(nums)-1] = nums[i+2:]
                nums[-1] = temp
            else:
                i += 1
        nums = nums[:lenDup]
        return len(nums)





if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    # nums = [1,1,2]
    # nums = [2]
    # nums = [1,1]
    res = Solution().removeDuplicates(nums)
    # res = nums[1:]
    print(nums)
    print(res)