class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeroNum, oneNum=0, 0
        zeroMaxNum, oneMaxNum = 0, 0
        for i in s:
            if i == "1":
                oneNum += 1
                if zeroNum != 0:
                    zeroMaxNum = max(zeroMaxNum, zeroNum)
                    zeroNum = 0
            elif i == "0":
                zeroNum += 1
                if oneNum != 0:
                    oneMaxNum = max(oneMaxNum, oneNum)
                    oneNum = 0
            # print(oneNum,zeroNum,oneMaxNum,zeroMaxNum)
        # 遍历结束后最后一步判断
        if zeroNum != 0:
            zeroMaxNum = max(zeroMaxNum, zeroNum)
            zeroNum = 0
        if oneNum != 0:
            oneMaxNum = max(oneMaxNum, oneNum)
            oneNum = 0

        if oneMaxNum > zeroMaxNum:
            return True
        else:
            return False

if __name__ == '__main__':
    # s = "1101"
    # s = "111000"
    s = "110100010"
    ret = Solution().checkZeroOnes(s)
    print(ret)