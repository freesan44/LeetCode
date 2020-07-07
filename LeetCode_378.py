class Solution:
    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        ##暴力法
        mLen = len(matrix)
        tempList = []
        for i in range(mLen):
            for j in range(mLen):
                tempList.append(matrix[i][j])
        tempList.sort()
        return tempList[k-1]

if __name__ == '__main__':
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    k = 8
    ret = Solution().kthSmallest(matrix, k)
    print(ret)