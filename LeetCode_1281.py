class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sList = list(map(int,list(str(n))))
        # print(sList)
        ji = 1
        he = 0
        for i in sList:
            ji *= i
            he += i
        return ji-he