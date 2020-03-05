# class Solution:
#     def longestCommonPrefix(self, strs: [str]) -> str:
#         # if len(strs) <= 0: return ""
#         # minLength = len(strs[0])
#         # startStr = strs[0]
#         # i = 0
#         # while i < minLength:
#         #     i += 1
#         #     for j in range(1,len(strs)):
#         #         jStr = strs[j]
#         #         if len(jStr) < minLength:
#         #             minLength = len(jStr)
#         #         print(startStr[:i])
#         #         print(jStr[:i])
#         #         if startStr[:i] != jStr[:i]:
#         #             i -= 1
#         #             print(i)
#         #             minLength = i
#         #             break
#         # return startStr[:i]
#         return ""
#     #比较字符长度
#     def isCommonPrefix(self, strs:[str], length:int) ->bool:
#         subStr = strs[0][:length]
#         for i in range(1,len(strs)):
#             if strs[i][:length] != subStr:
#                 return False
#         return True

#二分查找法
# class Solution:
#     def longestCommonPrefix(self, strs: [str]) -> str:
#         if len(strs) <=0 : return ""
#         import sys
#         minLen = sys.maxsize
#         for each in strs:
#             if len(each)<minLen:
#                 minLen = len(each)
#         low = 1
#         height = minLen
#         while low <= height:
#             middle = (low + height)//2
#             if self.isCommonPrefix(strs,middle) :
#                 low = middle +1
#             else:
#                 height = middle -1
#
#         return strs[0][0:(low+height)//2]
#     #比较字符长度
#     def isCommonPrefix(self, strs:[str], length:int) ->bool:
#         subStr = strs[0][:length]
#         for i in range(1,len(strs)):
#             if strs[i][:length] != subStr:
#                 return False
#         return True
#分治
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if len(strs) <= 0: return ""
        length = len(strs)
        return self.longestCommonPrefix2(strs, 0, length-1)


    def longestCommonPrefix2(self, strs: [str], left: int, right: int) ->str:
        if left == right:
            return strs[left]
        else:
            middle = (left + right) //2
            leftStr = self.longestCommonPrefix2(strs, left, middle)
            rightStr = self.longestCommonPrefix2(strs, middle+1,right)
            return self.isCommonPrefix(leftStr, rightStr)

    #比较字符长度
    def isCommonPrefix(self, leftStr: str, rightStr: str) ->str:
        minLen = min(len(leftStr),len(rightStr))
        for i in range(1, minLen+1):
            # print(i)
            # print(leftStr[:i])
            # print(rightStr[:i])
            if leftStr[:i] != rightStr[:i]:
                return leftStr[:i-1]
        return leftStr[:minLen]



if __name__ == '__main__':
    # result = Solution().longestCommonPrefix(["a", "b"])
    result = Solution().longestCommonPrefix(["flower","flow","flight","flower","flow","flight"])
    print(result)
