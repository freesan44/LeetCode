class Solution:
    def countSubTrees(self, n: int, edges: [[int]], labels: str) -> [int]:
        import collections
        listLab = list(labels)
        cacheList = [[i] for i in listLab]#字母存储数组
        # print(sum([i.count(3) for i in edges]))
        while len(edges)>0:
            tempList = edges.pop()
            leftNum = tempList[0]
            rightNum = tempList[1]
            if sum([i.count(rightNum) for i in edges]) != 0:
                leftNum, rightNum = rightNum, leftNum
            if rightNum == 0:##边界条件
                leftNum, rightNum = rightNum, leftNum
            cacheList[leftNum] = cacheList[leftNum] +cacheList[rightNum]
        # print(cacheList)
        ret = []
        for idx,val in enumerate(cacheList):
            countList = collections.Counter(val)
            count = countList[listLab[idx]]
            ret.append(count)
        return ret



if __name__ == '__main__':
    # n = 4
    # edges = [[0,1],[1,2],[0,3]]
    # labels = "bbbb"
    # n = 7
    # edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    # labels = "abaedcd"
    # n = 5
    # edges = [[0, 1], [0, 2], [1, 3], [0, 4]]
    # labels = "aabab"
    # n = 4
    # edges = [[0, 2], [0, 3], [1, 2]]
    # labels = "aeed"
    n = 25
    edges = [[4, 0], [5, 4], [12, 5], [3, 12], [18, 3], [10, 18], [8, 5], [16, 8], [14, 16], [13, 16], [9, 13], [22, 9], [2, 5],
     [6, 2], [1, 6], [11, 1], [15, 11], [20, 11], [7, 20], [19, 1], [17, 19], [23, 19], [24, 2], [21, 24]]
    labels = "hcheiavadwjctaortvpsflssg"
    result = Solution().countSubTrees(n, edges, labels)
    print(result)