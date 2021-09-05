class Solution:
    def numberOfSteps(self, num: int) -> int:
        # 迭代法
        # res = 0
        # while num != 0:
        #     if num % 2 == 0:
        #         num //= 2
        #         res += 1
        #     else:
        #         num -= 1
        #         res += 1
        # return res
        # 二进制（变成0的操作方法和变成二进制的辗转相除法很相近）
        if num == 0:
            return 0
        return bin(num).count("1") + num.bit_length()-1

if __name__ == '__main__':
    num = 14
    ret = Solution().numberOfSteps(num)
    print(ret)