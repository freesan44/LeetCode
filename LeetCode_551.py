class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") <= 1 and s.count("LLL")<=0:
            return True
        else:
            return False


if __name__ == '__main__':
    # s = "PPALLP"
    # s = "PPALLL"
    s = "LALLL"
    ret = Solution().checkRecord(s)
    print(ret)
