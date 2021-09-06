class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 通过遍历和count（1）组成一一对应数组，然后排序输出
        countList = [[index, val.count(1)] for index,val in enumerate(mat)]
        # for index,val in enumerate(mat):
        #     print(index,val)
        countList.sort(key=lambda x: (x[1], x[0]))
        resList = [i[0] for i in countList]
        return resList[:k]

if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0],
     [1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [1, 1, 1, 1, 1]]
    k = 3
    ret = Solution().kWeakestRows(mat, k)
    print(ret)