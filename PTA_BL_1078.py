type = input()
# type = "C"
# type = "D"

if type == "C":
    inputStr = input()
    # inputStr = "TTTTThhiiiis isssss a   tesssst CAaaa as"
    tempStr = inputStr[0]
    tempNum = 0
    res = ""
    for i in inputStr:
        if i == tempStr:
            tempNum += 1
        else:
            if tempNum == 1:
                res += tempStr
            else:
                res += str(tempNum)+tempStr
            tempStr = i
            tempNum = 1
    if tempNum == 1:
        res += tempStr
    else:
        res += str(tempNum) + tempStr
    print(res)
elif type == "D":
    inputStr = input()
    # inputStr = "5T2h4is i5s a3 te4st CA3a as10Z"
    tempStr = inputStr[0]
    tempNum = ""
    res = ""
    for i in inputStr:
        if i.isnumeric():
            tempNum += i
        else:
            tempStr = i
            if len(tempNum) == 0:
                res += tempStr
            else:
                res += tempStr*int(tempNum)
            tempNum = ""
    print(res)