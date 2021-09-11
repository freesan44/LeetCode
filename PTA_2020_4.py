N = int(input())
# N = int("305")

isChaoguo = False
resList = [0,1]
while isChaoguo == False:
    next = resList[-1]+ resList[-2]
    resList.append(next)
    # print(resList)
    if next >= N:
        isChaoguo = True
if abs(resList[-1]-N) >= abs(resList[-2]-N):
    print(resList[-2])
else:
    print(resList[-1])
