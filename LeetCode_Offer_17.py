class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = n*"9"
        return [i for i in range(1, int(res)+1)]

if __name__ == '__main__':
    n = 1
    result = Solution().printNumbers(n)
    print(result)