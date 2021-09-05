class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        #先抽取X坐标形成List排序，然后求差值
        XPoints = [i for i,_ in points]
        XPoints.sort(reverse=True)
        for index,val in enumerate(XPoints):
            if index != (len(XPoints)-1):
                XPoints[index] = XPoints[index]-XPoints[index+1]
        # print(XPoints[:-1])
        return max(XPoints[:-1])


if __name__ == '__main__':
    points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    ret = Solution().maxWidthOfVerticalArea(points)
    print(ret)