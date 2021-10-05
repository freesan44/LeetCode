class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sList = s.split("-")
        sStr =  "".join(sList)
        tempStr = ""
        res = []
        sStr = reversed(sStr)
        for i in sStr:
            if len(tempStr) == k:
                res.append(tempStr)
                tempStr = ""
            upperStr = i.upper()
            tempStr = upperStr + tempStr
        if len(tempStr) != 0:
            res.append(tempStr)
        res = res[::-1]
        # print(res)
        return "-".join(res)

if __name__ == '__main__':
    S = "5F3Z-2e-9-w"
    K = 4
    # S = "2-5g-3-J"
    # K = 2
    # S = "2-4A0r7-4k"
    # K = 4
    ret = Solution().licenseKeyFormatting(S, K)
    print(ret)