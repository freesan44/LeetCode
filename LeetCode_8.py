class Solution:
    def myAtoi(self, str: str) -> int:
        #常规解法
        # sList = list(str)
        # sLen = len(sList)
        # if sLen <= 0: return 0
        # checkFirst = False#检查空字符串开关
        # tempList = []
        # for i in range(sLen):
        #     if str[i] == " " and checkFirst == False:
        #         continue
        #     if checkFirst == False:
        #         # print(str[i])
        #         if str[i].isdigit() or str[i] == "-" or str[i] == "+":
        #             checkFirst = True
        #             tempList.append(str[i])
        #         else:
        #             return 0
        #     else:
        #         if str[i].isdigit():
        #             tempList.append(str[i])
        #         else:
        #             break
        # tempStr = "".join(tempList)
        # try:
        #     tempInt = int(tempStr)
        #     if tempInt > pow(2, 31)-1: return pow(2, 31)-1
        #     if tempInt < -pow(2, 31): return -pow(2, 31)
        # except:
        #     return 0
        # return tempInt
        #正则表达式
        import re
        match = re.match("[ ]*([+-]?\d+)",str)
        if not match: return 0
        res = int(match.group(1))
        return min(max(res, -pow(2, 31)),pow(2, 31)-1)



if __name__ == '__main__':
    # str = "words and 987"
    # str = "4193 with words"
    # str = "   -42"
    # str = "-91283472332"
    str = ""
    str = "+"
    str = "   +0 123"
    str = "2147483648"
    ret = Solution().myAtoi(str)
    print(ret)