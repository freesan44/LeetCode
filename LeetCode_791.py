class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ret = ""
        sList = list(s)
        for i in order:
            # print(i)
            while True:
                # 利用remove的特性，把對應字母刪增，直到沒法進行為止
                try:
                    sList.remove(i)
                    ret += i
                    # print(ret)
                except:
                    break
        ret += "".join(sList)
        return ret



if __name__ == '__main__':
    S = "cba"
    T = "abcddd"
    ret = Solution().customSortString(S, T)
    print(ret)