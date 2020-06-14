class Solution:
    def minDays(self, bloomDay: [int], m: int, k: int) -> int:
        ret = -1
        #进行倒数的数组
        countSet = sorted(set(bloomDay))
        for i in countSet:
            # print(i)
            tempM = m
            left = 0
            right = left+k
            # for j in range(len(bloomDay)):
            while tempM > 0:
                # print(bloomDay[left:right])
                if max(bloomDay[left:right]) <= i:
                    tempM -= 1
                    left = right
                    right = left+k
                else:
                    left += 1
                    right = left + k
                if right > len(bloomDay):break
            if tempM == 0:
                return i
        return ret
if __name__ == '__main__':
    # bloomDay = [1, 10, 3, 10, 2]
    # m = 3
    # k = 1
    # bloomDay = [7, 7, 7, 7, 12, 7, 7]
    # m = 2
    # k = 3
    # bloomDay = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    # m = 4
    # k = 2
    bloomDay = [1000000000, 1000000000]
    m = 1
    k = 1
    ret = Solution().minDays(bloomDay, m, k)
    print(ret)