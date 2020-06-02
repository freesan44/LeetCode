class Solution:
    def transpose(self, A: [[int]]) -> [[int]]:
        res = [[0]*len(A) for i in range(len(A[0]))]
        for i in range(len(A)) :
            for j in range(len(A[i])):
                res[j][i] = A[i][j]
        return res


if __name__ == '__main__':
    # nums = [[1,2,3],[4,5,6],[7,8,9]]
    nums = [[1,2,3],[4,5,6]]
    ret = Solution().transpose(nums)
    print(ret)