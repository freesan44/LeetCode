class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lenM = len(matrix)
        for i in range(lenM):
            for j in range(i+1, lenM):
                matrix[i][j] ,matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(lenM):
            matrix[i].reverse()#进行倒序




if __name__ == '__main__':
    matrix =[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    # nums = [4,3,2,1]
    res = Solution().rotate(matrix)
    print(res)