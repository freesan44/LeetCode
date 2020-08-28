class Solution:
    def judgeCircle(self, moves: str) -> bool:
        X = 0
        Y = 0
        movesList = list(moves)
        for each in movesList:
            if each == "R":
                X = X + 1
            elif each == "L":
                X = X - 1
            elif each == "U":
                Y = Y + 1
            elif each == "D":
                Y = Y - 1
        if X == 0 and Y == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    moves = "UD"
    moves = "LL"
    result = Solution().judgeCircle(moves)
    print(result)