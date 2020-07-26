class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        #成型
        sList = list(s)
        preCount = 0
        preS = ''
        proRet = ''
        countK = k
        countList = []#计算数字次数
        for i in sList:
            if i != preS and len(preS)>0:
                proRet = proRet + preS + str(preCount if preCount>1 else '')
                countList.append(preCount)
                preCount = 1
            else:
                preCount = preCount + 1
            preS = i
        #最后元素
        proRet = proRet + preS + str(preCount if preCount>1 else '')
        countList.append(preCount)
        #进行数据处理
        import collections
        counter = collections.Counter(countList)
        print(proRet)
        #把单符号的去掉
        countK = k - counter[1]
        if countK <= 0:
            return len(proRet)-k
        ret = len(proRet) - counter[1]
        tenList = []
        singleList = []
        for i in countList:
            if i >= 10:
                tenList.append(i-9)
            elif i <10 and i != 1:
                singleList.append(i)
        # tenList.sort(reverse=True)
        #需要扣除的进行排序
        tenList.sort(reverse=True)
        singleList.sort(reverse=True)
        print("{} {}".format(singleList, tenList))
        tempTen = None
        tempSingle = None
        while True:
            if tempTen == None:
                try:
                    tempTen = tenList.pop()
                except:
                    tempTen = 101
            if tempSingle == None:
                try:
                    tempSingle = singleList.pop()
                except:
                    tempSingle = 101
            #优先删除两个字符的
            if tempSingle<=tempTen:
                countK = countK - tempSingle
                if countK >= 0:
                    tempSingle = None
                    ret = ret - 2
            else:
                countK = countK - tempTen
                if countK >= 0:
                    tempTen = None
                    ret = ret - 1
            if countK <= 0:#扣除进位失败
                return ret



        return 0
if __name__ == '__main__':
    # s = "aaabcccd"
    # k = 2
    s = "aabbaa"
    k = 2
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbcccccccccccccccccccccccccccccd"
    # k = 4
    result = Solution().getLengthOfOptimalCompression(s, k)
    print(result)