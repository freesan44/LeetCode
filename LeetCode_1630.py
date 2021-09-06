class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # 暴力法
        # fanweiList = [(l[i], r[i]) for i in range(len(l))]
        fanweiList = zip(l,r)
        resList = []
        from collections import Counter
        for x,y in fanweiList:
            #抽取指定子数组并排序
            newNums = sorted(nums[x:y+1])
            # print(newNums)
            #用zip进行错位压缩，然后xy互减，形成等差数组，再通过Counter得出是否只有一个值，判断是否为等差
            zipList = list(zip(newNums[:],newNums[1:]))
            dengchaList = [y-x for x, y in zipList]
            resCount = Counter(dengchaList)
            if len(resCount) == 1:
                resList.append(True)
            else:
                resList.append(False)
        return resList


if __name__ == '__main__':
    nums = [4,6,5,9,3,7]
    l = [0,0,2]
    r = [2,3,5]
    ret = Solution().checkArithmeticSubarrays(nums, l, r)
    print(ret)