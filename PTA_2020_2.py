N = int(input())
KList = input().split()
# N = int("12")
# KList = "23 16 87 233 87 16 87 233 23 87 233 16".split()

from collections import Counter
countK = Counter(KList)
for key,val in countK.items():
    # print(key,val)
    if int(key)%2 == 1 and val %2 ==1:
        print(key)
# print(countK)