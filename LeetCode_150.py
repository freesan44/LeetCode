class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        # tokens.reverse()
        # #把所有倒序后的符号index抽出来，然后逐个推栈计算
        # tokenList = [i for i in range(len(tokens)) if tokens[i] == "+"or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/"]
        # for codeIndex in tokenList[::-1]:
        #     num1 = tokens.pop(codeIndex+2)
        #     num2 = tokens.pop(codeIndex+1)
        #     code = tokens.pop(codeIndex)
        #     # print("{},{},{}".format(num1,num2,code))
        #     tokens.insert(codeIndex ,self.dealWith2Num(code, num1, num2))
        # return int(tokens[-1])
        ##逐个遍历
        stack = []
        nontation = ["-","+","*","/"]
        for index,value in enumerate(tokens):
            if value in nontation:
                num1 = stack.pop()
                num2 = stack.pop()
                # print("{},{},{}".format(num2, num1, value))
                ret = self.dealWith2Num(value,num2,num1)
                stack.append(ret)
            else:
                stack.append(value)
        return int(stack[0])

    def dealWith2Num(self, code:str, num1:str, num2:str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        if code == "+":
            return str(num1 + num2)
        if code == "-":
            return str(num1 - num2)
        if code == "*":
            return str(num1 * num2)
        if code == "/":
            return str(int(num1 / num2))

if __name__ == '__main__':
    # nums = ["2", "1", "+", "3", "*"]
    nums = ["4", "13", "5", "/", "+"]
    nums = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ret = Solution().evalRPN(nums)
    print(ret)
