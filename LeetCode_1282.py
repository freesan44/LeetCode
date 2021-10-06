class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict
        resDict = defaultdict(list)
        #根据用户组的数量进行粗分组
        for index,val in enumerate(groupSizes):
            resDict[val].append(index)
        resList = []
        #根据key为数量进行细分组，把相同分组的分成多个小
        for key,valList in resDict.items():
            tempNum = 0
            tempList = []
            while len(valList)!= 0:
                tempNum += 1
                tempList.append(valList.pop())
                if tempNum % key == 0:
                    resList.append(tempList)
                    tempList = []
        return resList



if __name__ == '__main__':
    groupSizes = [3,3,3,3,3,1,3]
    ret = Solution().groupThePeople(groupSizes)
    print(ret)