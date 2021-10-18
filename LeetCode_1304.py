class Solution:
    def sumZero(self, n: int) -> List[int]:
        resList = []
        for i in range(n//2):
            resList.append(i+1)
            resList.append(-i-1)
        if n%2 == 1:resList.append(0)
        return resList



if __name__ == '__main__':
    n = 5
    ret = Solution().sumZero(n)
    print(ret)