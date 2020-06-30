class Solution:
    def canArrange(self, arr: [int], k: int) -> bool:
        print(sum(arr)%k)
        if sum(arr)%k != 0:
            return False
        return True


if __name__ == '__main__':
    arr = [1,2,3,4,5,10,6,7,8,9]
    k = 5
    arr = [1, 2, 3, 4, 5, 6]
    k = 10
    arr = [1, 2, 3, 4, 5, 6]
    k = 7
    ret = Solution().canArrange(arr, k)
    print(ret)
