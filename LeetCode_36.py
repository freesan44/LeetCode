class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        lines = [[] for i in range(9)] #横数组
        rows = [[] for i in range(9)] #竖数组
        block = [[] for i in range(9)]#九宫格
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != ".":
                    lines[i].append(board[i][j])
                    rows[j].append(board[i][j])
                    block[i//3*3+j//3].append(board[i][j])
        for line in lines:
            if len(line) != len(set(line)):
                return False
        for row in rows:
            if len(row) != len(set(row)):
                return False
        for bl in block:
            if len(bl) != len(set(bl)):
                return False


        return True



if __name__ == '__main__':
    board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # nums = [4,3,2,1]
    res = Solution().isValidSudoku(board)
    print(res)