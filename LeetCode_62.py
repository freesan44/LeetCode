class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # countGrid = [[0]*m for i in range(n)]
        # for i in range(m):
        #     countGrid[0][i] = 1
        # for j in range(n):
        #     countGrid[j][0] = 1
        # #动态规划，每个元素的最多路线，是为上部+左部
        # for i in range(1,m):
        #     for j in range(1,n):
        #         countGrid[j][i] = countGrid[j-1][i] + countGrid[j][i-1]
        # # print(countGrid)
        # return countGrid[n-1][m-1]
        #优化动态规划的空间,因为是前一列加上当前列的前一个元素，可以缩减为一个数组
        countList = [1]*n
        for i in range(1, m):
            for i in range(1, n):
                countList[i] = countList[i-1] + countList[i]
        print(countList)
        return countList[-1]

if __name__ == '__main__':
    # m = 3
    # n = 2
    m = 7
    n = 3
    result = Solution().uniquePaths(m, n)
    print(result)