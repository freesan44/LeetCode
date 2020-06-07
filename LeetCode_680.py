class Solution:
    def validPalindrome(self, s: str) -> bool:
        # #常规解法(超出时间)
        # sList = list(s)
        # sLen = len(s)
        # if sList[:] == sList[::-1]:
        #     return True
        # for i in range(sLen):
        #     temp = sList.copy()
        #     temp.pop(i)
        #     if temp[:] == temp[::-1]:
        #         return True
        # return False
        #双指针
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]:
                print(s[left+1:right+1])
                print(s[left:right])
                return True
            else:
                return False
        return True



if __name__ == '__main__':
    str = "abca"
    str = "abc"
    # str = "aguokepatgbnvfqqfvnbgtapekouga"
    # str = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    ret = Solution().validPalindrome(str)
    print(ret)