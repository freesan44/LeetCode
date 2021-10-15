class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # # 超时
        # if len(nums) <= 1:
        #     return nums
        # pivot = nums[0]
        # right,left = [],[]
        # for each in nums[1:]:
        #     if each <= pivot:
        #         left.append(each)
        #     else:
        #         right.append(each)
        # return self.sortArray(left) + [pivot] + self.sortArray(right)
        # 快速排序，采用随机pivot
        from random import randint
        if len(nums) <= 1:
            return nums
        randNum = randint(0,len(nums)-1)
        pivot = nums[randNum]
        right, left = [], []
        for index,each in enumerate(nums):
            if index == randNum:continue
            if each <= pivot:
                left.append(each)
            else:
                right.append(each)
        return self.sortArray(left) + [pivot] + self.sortArray(right)

    #     #快速排序
    #     self.quickSort(nums,0,len(nums)-1)
    #     return nums
    #
    # def quickSort(self, nums, left, right):
    #     from random import randint
    #     pivot = nums[randint(left,right)]
    #     i,j = left, right
    #     while i<=j:
    #         # print(i,j,nums)
    #         while nums[i]<pivot:
    #             i += 1
    #         while nums[j]>pivot:
    #             j -= 1
    #         if i<=j:
    #             nums[i],nums[j] = nums[j],nums[i]
    #             i += 1
    #             j -= 1
    #     if i < right:
    #         self.quickSort(nums, i, right)
    #     if j > left:
    #         self.quickSort(nums,left, j)




if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    ret = Solution().sortArray(nums)
    print(ret)