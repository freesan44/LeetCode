N = map(int, input())
NList = list(map(int, input().split()))

# N = map(int, "5")
# NList = list(map(int, "1 3 2 4 5".split()))
# N = map(int, "0")
# NList = list(map(int, "".split()))

## 该方法超时
# resList = []
# for index,val in enumerate(NList):
#     # print(NList[:index],val)
#     # print(NList[index+1:])
#     leftList = NList[:index]
#     rightList = NList[index+1:]
#     if len(leftList) == 0 and len(rightList) == 0:
#         break
#     if (len(leftList) == 0 and min(rightList) > val) or (len(rightList) == 0 and max(leftList) < val):
#         resList.append(val)
#     elif max(leftList) < val  and min(rightList) > val:
#         resList.append(val)
# if len(resList) == 0:
#     print("0")
#     print("")
# else:
#     resList.sort()
#     resStrList = list(map(str,resList))
#     print(len(resStrList))
#     print(" ".join(resStrList))

resList = []
sourtList = sorted(NList)
max = 0 #存储最大值，这样可以跳过部分不符合的元素判断
for i in range(len(NList)):
    if NList[i] > max:
        max = NList[i]
        if NList[i] == sourtList[i]:#因为每个元素不同，那么排序后的元素位置和原来位置应该相同，不然肯定存在左右不符的情况
            resList.append(NList[i])
if len(resList) == 0:
    print("0")
    print("")
else:
    resList.sort()
    resStrList = list(map(str,resList))
    print(len(resStrList))
    print(" ".join(resStrList))


