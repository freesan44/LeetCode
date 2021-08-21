def checkIsHuiwen(num: int) -> bool:
    numStr = str(num)
    for i in range(len(numStr)//2):
        # print(str(numStr[i]) + " " + str(numStr[len(numStr)-1-i]))
        if numStr[i] != numStr[len(numStr)-1-i]:
            return False
    return True
inputStr = str(input())
# inputStr = str(101)
res = inputStr
hasRes = False
for i in range(10):
    if checkIsHuiwen(int(res)):
        print(res + " is a palindromic number.")
        hasRes = True
        break
    else :
        num1 = int(res)
        num2 = int(res[::-1])
        resNum = num1 + num2
        print(str(num1) + " + " + str(num2) + " = " + str(resNum))
        res = str(resNum)

if hasRes == False:
    print("Not found in 10 iterations.")

