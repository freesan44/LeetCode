class Solution:
    def getStrongest(self, arr: [int], k: int) -> [int]:
        arr.sort()
        ret = []
        midNum = arr[(len(arr)-1)//2]
        print(midNum)
        left = 0
        right = len(arr)-1
        while left <= right:
            if abs(arr[left] - midNum) > abs(arr[right]-midNum):
                ret.append(arr[left])
                left += 1
            else:
                ret.append(arr[right])
                right -= 1
            if len(ret) == k:
                break
        return ret


if __name__ == '__main__':
    arr = [6,-3,7,2,11]
    arr = [-7,22,17,3]
    arr = [6,7,11,7,6,8]
    k = 3
    ret = Solution().getStrongest(arr, k)
    print(ret)