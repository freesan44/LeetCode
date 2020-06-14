class Solution:
    def findLeastNumOfUniqueInts(self, arr: [int], k: int) -> int:
        import collections
        countDic = dict(collections.Counter(arr).most_common())
        # print(countDic)
        # retList = list(countDic)
        # print(retList)
        # return len(set(retList[k:]))
        resKeyList = list(countDic.keys())
        resKeyList.reverse()
        for i in resKeyList:
            count = countDic[i]
            k -= count
            if k >= 0:
                countDic.pop(i)
                # print(countDic)
            if k < 0:
                break
        return len(countDic)
if __name__ == '__main__':
    arr = [4,3,1,1,3,3,2]
    k = 3
    # arr = [2, 1, 1, 3, 3, 3]
    # k = 3
    arr = [2, 4, 1, 8, 3, 5, 1, 3]
    k = 3
    ret = Solution().findLeastNumOfUniqueInts(arr, k)
    print(ret)