class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        rowLen = len(obstacleGrid)
        colLen = len(obstacleGrid[0])
        if rowLen==1 and colLen==1:#边界条件
            return 1 if obstacleGrid[0][0] ==0 else 0
        #起点终点有阻碍就直接终止
        if obstacleGrid[rowLen-1][colLen-1]==1 or obstacleGrid[0][0]==1:
            return 0
        countGrid = [[0]*colLen for i in range(rowLen)]
        for i in range(rowLen):
            if obstacleGrid[i][0] == 1:break#对边边有阻碍，路线终止
            countGrid[i][0] = 1
        for j in range(colLen):
            if obstacleGrid[0][j] == 1: break#对边边有阻碍，路线终止
            countGrid[0][j] = 1
        for i in range(1, rowLen):
            for j in range(1, colLen):
                leftCount = countGrid[i-1][j] if obstacleGrid[i-1][j] == 0 else 0
                topCount = countGrid[i][j-1] if obstacleGrid[i][j-1] == 0 else 0
                countGrid[i][j] = leftCount + topCount
        # print(countGrid)
        return countGrid[rowLen-1][colLen-1]

if __name__ == '__main__':
  #   obstacleGrid = [
  # [0,0,0],
  # [0,1,0],
  # [0,0,0]
# ]
    # obstacleGrid = [
    #   [0,0,0],
    #   [0,1,0]
    # ]
    # obstacleGrid = [[1]]
    # obstacleGrid = [[0, 1]]
    obstacleGrid = [[0,0],[1,1],[0,0]]
    result = Solution().uniquePathsWithObstacles(obstacleGrid)
    print(result)