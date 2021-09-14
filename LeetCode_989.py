class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        #字符串与int的转换
        resStr = ""
        for i in num:
            resStr +=str(i)
        res = str(int(resStr)+k)
        reslist = []
        for i in res:
            reslist.append(int(i))
        return reslist

if __name__ == '__main__':
    A = [1,2,0,0]
    K = 34
    ret = Solution().addToArrayForm(A, K)
    print(ret)