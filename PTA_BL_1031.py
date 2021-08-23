count = int(input())
# count = int("4")
jiaquanList = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
jiaoyanMList = ["1","0","X","9","8","7","6","5","4","3","2"]
isAllPass = True
for i in range(count):
    inputStr = str(input())
    # inputStr = str("12010X198901011234")
    inputStrList = list(inputStr)
    countRes = 0
    if len(inputStrList) > 18:#超过18位跳过
        print(inputStr)
        isAllPass = False
        continue
    if inputStr[:-1].isdigit() == False:#判断不为数字则跳过
        print(inputStr)
        isAllPass = False
        continue
    for index, val in enumerate(inputStrList[:-1]):
        countRes += int(val) * jiaquanList[index]  # 加权系数是乘法非加法
    #对11取模 跟最后一位核对
    # print(countRes)
    resM = jiaoyanMList[countRes%11]
    if resM != inputStrList[-1]:
        print(inputStr)
        isAllPass = False
if isAllPass == True:
    print("All passed")


