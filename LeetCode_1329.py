class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row , col = len(mat), len(mat[0])
        # 配置遍历的初始点数组，然后进行遍历
        startPoints = [(0,x) for x in range(col)]+[ (y,0) for y in range(row)]
        startPoints.pop(0)#把重复的(0,0)去掉
        # print(startPoints)
        for x, y in startPoints:
            step = min(abs(row-1-x),abs(col-1-y))#先获取行走步数
            # 获取斜线数组
            lineList = [(x+i, y+i) for i in range(step+1)]
            # 获取斜线上全部数组的内容，然后排序，重新赋值
            pointList = [mat[i][j] for i,j in lineList]
            # print(pointList)
            pointList.sort()
            for i, j in lineList:
                mat[i][j] = pointList.pop(0)
        # print(mat)
        return mat

if __name__ == '__main__':
    mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    ret = Solution().diagonalSort(mat)
    print(ret)