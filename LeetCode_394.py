class Solution:
    def decodeString(self, s: str) -> str:
        sList = list(s)
        stack = list()
        res = ""
        while len(sList) != 0:
            i = sList.pop(0)
            # print(i)
            if i == "]":#出栈
                tempStr = ""#找出栈内最后一个[]内的字符串
                while True:
                    j = str(stack.pop())
                    if j.isalpha() == True:
                        tempStr = j + tempStr
                    elif j == "[":
                        break
                tempInt = ""#找出栈内最后一个连续数字
                # print(stack, tempStr, tempInt,"-")
                while True:
                    try:
                        k = stack.pop()
                        if k.isnumeric() == True:
                            tempInt = k + tempInt
                        else:
                            stack.append(k)#如果是非数字，再次入栈
                            break
                    except:#用于边界条件【其实不稳固】
                        break
                # print(stack,tempStr,tempInt)
                stack.append(tempStr*int(tempInt))
                # print(stack)
            else:
                stack.append(i)
                # print(stack)
        return "".join(stack)



if __name__ == '__main__':
    # s = "3[a]2[bc]"
    # s = "3[a2[c]]"
    # s = "2[abc]3[cd]ef"
    # s = "abc3[cd]xyz"
    s = "100[leetcode]"
    result = Solution().decodeString(s)
    print(result)


