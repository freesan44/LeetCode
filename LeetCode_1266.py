class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            x1, y1 = points[i - 1][0], points[i - 1][1]
            x2, y2 = points[i][0], points[i][1]
            res += max(abs(x1-x2), abs(y1-y2))##选择x,y绝对值的最大值
        return res


if __name__ == '__main__':
    points = [[1,1],[3,4],[-1,0]]
    points = [[3, 2], [-2, 2]]
    ret = Solution().minTimeToVisitAllPoints(points)
    print(ret)