class Solution:
    def flipAndInvertImage(self, A: [[int]]) -> [[int]]:
        res = []
        for eachList in A:
            #异或1
            newEachList = [each^1 for each in eachList]
            newEachList.reverse()
            res.append(newEachList)
        return res



if __name__ == '__main__':
    nums = [[1,1,0],[1,0,1],[0,0,0]]
    ret = Solution().flipAndInvertImage(nums)
    print(ret)