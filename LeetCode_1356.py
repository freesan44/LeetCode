class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        from collections import Counter
        # bin用于把字符转换成二进制
        # Counter用于收集里面有多少个1
        # 形成(值，1数量)的元素
        tupleList = [(x,(dict(Counter(bin(x)))).get("1",0)) for x in arr]
        # 根据先【1数量】再【值】的排序
        resTupleList = sorted(tupleList, key= lambda x: (x[1], x[0]))
        # print(resTupleList)
        resList = [x for x, _ in resTupleList]
        # print(resList)
        return resList

if __name__ == '__main__':
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    ret = Solution().sortByBits(arr)
    print(ret)