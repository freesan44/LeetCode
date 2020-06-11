class Solution:
    def heightChecker(self, heights: [int]) -> int:
        temList = sorted(heights)
        ret = 0
        for i in range(len(heights)):
            #替换次数，其实就是每个原来位置不一样的数值都要换一次，所以替换次数=同位置不同值的次数
            if heights[i] != temList[i]:
                ret += 1
        return ret

if __name__ == '__main__':
    heights = [1,1,4,2,1,3]
    ret = Solution().heightChecker(heights)
    print(ret)