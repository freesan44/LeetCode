class Solution:
    def compressString(self, S: str) -> str:
        sList = S
        if len(sList)<=1:
            return S
        tempCache = 1
        tempStr = sList[0]
        ret = ""
        for i in range(1,len(sList)):
            eachStr = sList[i]
            print(eachStr)
            if eachStr == tempStr:
                tempCache += 1
            else:

                ret = ret + tempStr + str(tempCache)
                tempCache = 1
            tempStr = eachStr
        ret = ret + tempStr + str(tempCache)
        if len(ret)>=len(sList):
            return S

        return ret

if __name__ == '__main__':
    testStr = "aabcccccaaa"
    testStr = "bb"
    ret = Solution().compressString(testStr)
    print(ret)
