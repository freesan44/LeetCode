class NumArray:
    # numArr = list()
    # snumArr = [0]
    def __init__(self, nums: List[int]):
        # self.numArr = list(nums)
        self.snumArr = [0]
        # 前缀和算法
        for index,val in enumerate(nums):
            self.snumArr.append(self.snumArr[index]+val)
            # print(self.snumArr)

    def sumRange(self, left: int, right: int) -> int:
        # 粗暴解法
        # print(left,right)
        # print(self.numArr[left:right])
        # return sum(self.numArr[left:right+1])
        # 前缀和算法
        self.snumArr.ex
        return self.snumArr[right+1] - self.snumArr[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# numArray = NumArray([-2, 0, 3, -5, 2, -1])
# print(numArray.sumRange(0, 2))
# print(numArray.sumRange(2, 5))
# print(numArray.sumRange(0, 5))
numArray = NumArray([-1])
print(numArray.sumRange(0, 0))