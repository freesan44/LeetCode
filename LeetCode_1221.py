class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # 用堆的形式实现
        tempList = []
        ret = 0
        for i in s:
            if len(tempList) == 0 or tempList[-1] == i:
                tempList.append(i)
            elif tempList[-1] != i:
                tempList.pop()
            if len(tempList) == 0:
                ret += 1
        return ret


if __name__ == '__main__':
    s = "RLRRLLRLRL"
    ret = Solution().balancedStringSplit(s)
    print(ret)