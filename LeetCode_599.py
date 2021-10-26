class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        resDict = dict()
        resList = list()
        for index,val in enumerate(list1):
            resDict[val] = index
        for index,val in enumerate(list2):
            if val in resDict:
                resList.append((index+resDict[val],val))
        #对index总和排序，得到最低权重的值，然后把相同值抽取出来
        resList.sort(key=lambda x:x[0])
        res = []
        resIndex = resList[0][0]
        for indexCount,val in resList:
            if indexCount == resIndex:
                res.append(val)
        return res

if __name__ == '__main__':
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    ret = Solution().findRestaurant(list1,list2)
    print(ret)