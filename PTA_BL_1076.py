inputCount = int(input())
# inputCount = int("8")
res = ""
for i in range(inputCount):
    inputList = list(input().split(" "))
    # inputList = list("A-T B-F C-F D-F".split(" "))
    for index,val in enumerate(inputList):
        if "T" in val:
            resNum = 0
            if val[0] == "A":
                resNum = 1
            elif val[0] == "B":
                resNum = 2
            elif val[0] == "C":
                resNum = 3
            elif val[0] == "D":
                resNum = 4
            res = res + str(resNum)
print(res)