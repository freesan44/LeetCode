class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lieList = []
        hengList = []
        for i in range(len(matrix)):
            lieList.append(min(matrix[i]))
        for j in range(len(matrix[0])):
            tempList = [x[j] for x in matrix]
            hengList.append(max(tempList))
        # print(lieList,hengList)
        return [x for x in lieList if x in hengList]


if __name__ == '__main__':
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    matrix = [[7, 8], [1, 2]]
    res = Solution().luckyNumbers(matrix)
    print(res)