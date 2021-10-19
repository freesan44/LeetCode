class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 0, x
        res = 0
        while left <= right:
            mid = (left + right)//2
            # print(mid,left,right)
            sqrtX = mid ** 2
            if sqrtX > x:
                right = mid -1
            else:
                res = mid
                left = mid + 1
        return res

if __name__ == '__main__':
    x = 4
    x = 8
    x = 1
    ret = Solution().mySqrt(x)
    print(ret)