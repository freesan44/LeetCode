class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # 因为不统计翻转次数，所以只要排序后顺序一样就行了
        target.sort()
        arr.sort()
        if target == arr:
            return True
        else:
            return False

if __name__ == '__main__':
    target = [1,2,3,4]
    arr = [2,4,1,3]
    target = [3, 7, 9]
    arr = [3, 7, 11]
    ret = Solution().canBeEqual(target, arr)
    print(ret)