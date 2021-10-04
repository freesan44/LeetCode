class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        length = len(points)
        from collections import defaultdict
        for i in range(length):
            resDict = defaultdict(int)
            for j in range(length):
                #把每个点与i的距离作为字段存储起来
                leng = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                resDict[leng] += 1
            count = 0
            #有多少个回力标，等于相同间距的数量k*(k-1)组合数
            for k in resDict.values():
                count += k*(k-1)
            res += count
        return res
if __name__ == '__main__':
    points = [[0,0],[1,0],[2,0]]
    points = [[1, 1], [2, 2], [3, 3]]
    points = [[1, 1]]
    ret = Solution().numberOfBoomerangs(points)
    print(ret)