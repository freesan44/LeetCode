class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        ## 获取全部字符串的个数
        countS = Counter(s)
        tupleList = [(x,y) for x,y in countS.items()]
        ## 转成数组，然后根据x[1]【数量】进行倒序排序，然后输出
        tupleList.sort(key=lambda x: x[1], reverse=True)
        resStr = ""
        for (val, count) in tupleList:
            resStr += val*count

        return resStr

if __name__ == '__main__':
    s = "tree"
    ret = Solution().frequencySort(s)
    print(ret)
