class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        newList = list(map(int, nums))
        newList.sort(reverse=True)
        # print(newList)
        return str(newList[k-1])

if __name__ == '__main__':
    nums = ["3","6","7","10"]
    k = 4
    # nums = ["2", "21", "12", "1"]
    # k = 3
    result = Solution().kthLargestNumber(nums, k)
    print(result)