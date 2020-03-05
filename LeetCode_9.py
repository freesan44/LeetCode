class Solution:
    def isPalindrome(self, x: int) -> bool:
        #字符串方法
        # y = str(x)[::-1]
        # if y == str(x):
        #     return True
        # else:
        #     return False
        #非字符串方法
        if x < 0:return False
        if x == 0:return True
        y = int()
        import math
        length = int(math.log(x, 10)) + 1
        for i in range(length//2):
            if x//10**(length - i*2 - 1) % 10 == x % 10:
                x //= 10
                print(x)
            else:
                return False
        return True

if __name__ == '__main__':
    result = Solution().isPalindrome(12345432)
    print(result)
