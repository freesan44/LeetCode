N = int(input())
# N = int("4")

inputList = []
for _ in range(N):
    name, ID, grade = map(str,input().split())
    # name, ID, grade = map(str, "Joe Math990112 89".split())
    inputList.append([name,ID,int(grade)])
grade1, grade2 = map(int,input().split())
# grade1, grade2 = map(int,"60 100".split())
resList = []
for each in inputList:
    if each[2]>= grade1 and each[2] <= grade2:
        resList.append(each)
# 排序输出
resList.sort(key=lambda x:-x[2])
if len(resList) == 0:
    print("NONE")
else:
    for each in resList:
        print(each[0],each[1])