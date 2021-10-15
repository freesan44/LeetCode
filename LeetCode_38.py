class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            temp = None
            count = 0
            tempStr = ""
            for i in s:
                if temp == i:
                    count += 1
                else:
                    if temp:
                        tempStr += str(count)+temp
                    temp = i
                    count = 1
            tempStr += str(count) + temp
            # print(tempStr)
            s = tempStr
        return s





if __name__ == '__main__':
    n = 10
    ret = Solution().countAndSay(n)
    print(ret)