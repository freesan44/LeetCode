inputStr = str(input())
# inputStr = str("233235")

if len(inputStr)%2 != 0:
    print("Error: "+str(len(inputStr))+" digit(s)")
else:
    length = len(inputStr)
    A1 = inputStr[:length//2]
    A2 = inputStr[length//2:]
    # print(A1,A2)
    A1Res,A2Res = 0,0
    for i in A1:
        A1Res += int(i)
    for i in A2:
        A2Res += int(i)
    # print(A1Res,A2Res)
    if (A2Res - A1Res) == 2:
        print("Yes: {} - {} = 2".format(A2, A1))
    else:
        print("No: {} - {} != 2".format(A2, A1))