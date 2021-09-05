class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        retList = []
        for i in arr2:
            ## 利用remove自动寻找值的特性，一直找到没空为止就跳出循环
            while True:
                try:
                    arr1.remove(i)
                    retList.append(i)
                except:
                    break
        retList += sorted(arr1)
        return retList

if __name__ == '__main__':
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    ret = Solution().relativeSortArray(arr1, arr2)
    print(ret)