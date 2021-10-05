M, N = map(int,input().split())
# M, N = map(int,"5 3".split())
inputList = []
# from collections import defaultdict
# resDict = defaultdict(int)
for _ in range(N):
    eachInput = list(map(int, input().split()))
    # eachInput = list(map(int, "24 24 0 0 24".split()))
    # for i in eachInput:
    #     resDict[i] += 1
        # inputList.append(i)
    inputList += eachInput

# from collections import Counter
# counter = Counter(inputList).most_common(1)
# print(resDict)
# counter = Counter(resDict).most_common(1)
length = len(inputList)
inputList.sort()
print(inputList[length//2])
# print(counter[0][0])