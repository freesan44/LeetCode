class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        resArr = []
        # 针对每个圆
        for quer in queries:
            res = 0
            for point in points:
                a, b = point[0], point[1]
                X, Y, R = quer[0], quer[1], quer[2]
                # (X-a)^2+(Y-b)^2=r^2
                if (X-a)**2 + (Y-b)**2 <= R**2:
                    res += 1
            resArr.append(res)
        return resArr

if __name__ == '__main__':
    points = [[1,3],[3,3],[5,3],[2,2]]
    queries = [[2,3,1],[4,3,1],[1,1,2]]
    ret = Solution().countPoints(points, queries)
    print(ret)