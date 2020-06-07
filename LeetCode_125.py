class Solution:
    def isPalindrome(self, s: str) -> bool:
        #数组
        # sList = []
        # for i in s:
        #     if i.isalnum():#判断是否是字母
        #         sList.append(i.lower())#变成小写并写入
        # midNum = len(sList)//2
        # if sList[:midNum] == sList[::-1][:midNum]:
        #     return True
        # return False
        #双指针
        left = 0
        right = len(s)-1
        while right - left > 0:
            # print(s[left])
            # print(s[right])
            if s[left].isalnum() and s[right].isalnum() and s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            elif s[left].isalnum() == False:
                left += 1
            elif s[right].isalnum() == False:
                right -= 1
            else:
                return False
        return True



if __name__ == '__main__':
    str = "A man, a plan, a canal: Panama"
    str = "A man, a plan, a canal: Panama"
    ret = Solution().isPalindrome(str)
    print(ret)