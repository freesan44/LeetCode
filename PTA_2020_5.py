P = str(input())
S = str(input())
# P = str("atpaaabpabttpcat")
# S = str("pat")



def isCunzai(input:str, S:str) -> bool:
    j = 0
    for i in input:
        if i == S[j]:
            j += 1
            if len(S) == j:
                return True
    return False

resList = []
PList = list(P)
left0 = S[0]
right0 = S[-1]
left0List = []
right0List = []
for index,val in enumerate(PList):
    if val == left0:
        left0List.append(index)
    if val == right0:
        right0List.append(index)
minLeng = len(P)
for i in left0List:
    for j in right0List:
        # print(i,j,P[i:j+1])
        length = j +1  - i
        if i<=j and length <= minLeng:
            PtempStr = (P[i:j+1])
            if isCunzai(PtempStr,S) == True:
                resList.append(PtempStr)
                minLeng = len(PtempStr)
                break
# print(resList)
print(min(resList,key= lambda x:len(x)))

