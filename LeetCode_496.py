class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        resDict = dict()
        stack = list()
        #先通过倒序，用单调栈来保存最大值
        for i in nums2[::-1]:
            #栈里有值，代表目标的右边有大值
            while len(stack)>0:
                #判断右边的大值是否比自身大，大就保存结果，否则就pop
                if stack[-1]>i:
                    resDict[i] = stack[-1]
                    break
                else:
                    stack.pop()
            #把自身扔到栈里面
            stack.append(i)
            #右边没找到比自己大的，直接-1保存
            if i not in resDict:resDict[i] = -1
        res = list()
        for j in nums1:
            res.append(resDict[j])
        return res

if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    result = Solution().nextGreaterElement(nums1,nums2)
    print(result)