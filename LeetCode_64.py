class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        rowLen = len(grid[0])
        colLen = len(grid)
        countGrid = [[0]*rowLen for i in range(colLen)]#初始化统计步数矩阵
        countGrid[0][0] = grid[0][0]
        for i in range(1, rowLen):
            countGrid[0][i] = countGrid[0][i-1] + grid[0][i]
        for j in range(1, colLen):
            countGrid[j][0] = countGrid[j-1][0] + grid[j][0]
        # print(countGrid)
        for i in range(1, rowLen):##每个步数元素，存储从左边和上边的最小值，再加上自身的值，为自己所在元素的最小步数
            for j in range(1, colLen):
                # print("{} {}".format(j, i))
                countGrid[j][i] = min(countGrid[j][i-1], countGrid[j-1][i]) + grid[j][i]

        return countGrid[colLen-1][rowLen-1]

if __name__ == '__main__':
#     grid = [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
    grid = [[1,2,5],[3,2,1]]
    result = Solution().minPathSum(grid)
    print(result)