class Solution:
    def romanToInt(self, s: str) -> int:
        # num = int()
        # strList = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
        # numList = [4, 9, 40, 90, 400, 900, 1, 5, 10, 50, 100, 500, 1000]
        # while len(s)>0:
        #     for i in range(len(strList)):
        #         if s.find(strList[i]) >= 0:
        #             num += numList[i]
        #             s = s.replace(strList[i], '', 1)
        #             break
        # return num
        num = int()
        numList = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sList = list(s)
        for i in range(len(sList)-1):
            newInt = numList[sList[i]]
            nextInt = numList[sList[i+1]]
            if newInt >= nextInt:
                num += newInt
            else:
                num -= newInt
        num +=  numList[sList[-1]]
        return num




if __name__ == '__main__':
    result = Solution().romanToInt("III")
    print(result)
