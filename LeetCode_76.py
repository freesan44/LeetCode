class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        length = len(s)
        left,right,match = 0, 0,0
        resLeft,resRight,minResLen = 0, 0,length+1
        tDict = Counter(t)
        while right < length:
            #先右边扩张
            # print(left, right, resLeft, resRight)
            # print([s[left:right+1]])
            rS = s[right]
            # print(rS,tDict)
            if rS in tDict:
                tDict[rS] -= 1
                if tDict[rS] >= 0:
                    match += 1
            #收缩条件
            while match == len(t):
                #判断是否最短子串长度
                if (right - left) < minResLen:
                    # print([s[left:right + 1]],resRight,resLeft, minResLen)
                    minResLen = min(minResLen,right-left)
                    resLeft,resRight = left,right
                #左边在收缩，直到mtath<len(t)
                if left <= right:
                    lS = s[left]
                    if lS in tDict:
                        tDict[lS] += 1
                        if tDict[lS] > 0:
                            match -= 1
                        # print(lS, tDict)
                    left += 1
            right += 1
        # print(left, right, resLeft, resRight)
        return s[resLeft:resRight+1] if minResLen != length+1 else ""

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    s = "a"
    t = "a"
    result = Solution().minWindow(s,t)
    print(result)