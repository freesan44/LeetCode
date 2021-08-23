inputList = list(input().split())
# inputList = list("3 2 8 5".split())
count = int(inputList.pop(0))
res = 0
for index1, val1 in enumerate(inputList):
    for index2, val2 in enumerate(inputList):
        if index1 != index2:
            #把个位十位从Str转成int
            res = res + int(str(val1+val2))
print(res)
