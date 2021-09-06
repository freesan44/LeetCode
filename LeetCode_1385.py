class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # # 暴力解法
        # ret = 0
        # for i in arr1:
        #     resList = [abs(j-i) for j in arr2]
        #     # print(resList,min(resList))
        #     if min(resList) > d:
        #         ret += 1
        # return ret
        #二分查找法
        ret = 0
        arr2.sort()
        import bisect
        for i in arr1:
            left = bisect.bisect_left(arr2, i-d)
            right = bisect.bisect(arr2, i+d)
            print(arr2,left,right)
            if left == right:
                ret += 1
        return ret

if __name__ == '__main__':
    # arr1 = [4,5,8]
    # arr2 = [10,9,1,8]
    # d = 2
    arr1 = [1, 4, 2, 3]
    arr2 = [-4, -3, 6, 10, 20, 30]
    d = 3
    ret = Solution().findTheDistanceValue(arr1, arr2, d)
    print(ret)