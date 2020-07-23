class Solution:
    def minArray(self, numbers: [int]) -> int:
        return min(numbers)

if __name__ == '__main__':
    numbers = [3,4,5,1,2]
    result = Solution().minArray(numbers)
    print(result)