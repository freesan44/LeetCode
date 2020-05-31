class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        # #转换成数字
        # strDig = [str(i) for i in digits]
        # intDig = int("".join(strDig))
        # intDig += 1
        # return [int(i) for i in str(intDig)]
        #倒序
        digits.reverse()
        isPlus : bool = True# 是否需要进位
        for i in range(len(digits)):
            if isPlus == True:
                if digits[i] == 9:
                    digits[i] = 0
                    isPlus = True
                    if i == len(digits)-1:#最后一位加个1
                        digits.append(1)
                else:
                    digits[i] += 1
                    isPlus = False
        digits.reverse()
        return digits




if __name__ == '__main__':
    nums = [1,2,3]
    # nums = [4,3,2,1]
    res = Solution().plusOne(nums)
    print(res)