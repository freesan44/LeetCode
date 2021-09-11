N = int(input())
inputList = list(input().split())
# N = int("10")
# inputList = list("1234 98 329 9552 47621 8862 5539 2333 5365 463".split())

resList = []
for i in inputList:
    res = 1
    for j in i:
        res = res * int(j)
    resList.append(res)
from collections import Counter
counter = Counter(resList).most_common()
counter.sort(key= lambda x:(-x[1],x[0]))
if len(counter) == 0:
    print("0")
else:
    print(len(counter),counter[0][0])