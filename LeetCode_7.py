class Solution:
    def reverse(self, x: int) -> int:
        Y = int();
        # length = len(strX)
        if x > 0:
            Y = int(str(x)[::-1])
        else:
            Y = -int(str(-x)[::-1])
        # for i in range(0,len(strX)):
        #     if strX[length - 1 - i] == '-':
        #         strY.insert(0,'-')
        #         continue
        #     strY += strX[length - 1 - i]
        # Y = int("".join(strY))
        if (Y < -2 ** 31 or Y > (2**31 - 1)):
            return  0
        return Y

if __name__ == '__main__':
    result = Solution().reverse(-12)
    print(result)
