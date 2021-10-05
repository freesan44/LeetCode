N = int(input())
inputList = list(map(int, input().split()))
# N = int("13")
# inputList = list(map(int, "110 79 218 69 3721 100 29 135 2 6 13 5188 85".split()))
# 排序后，从中间前后分割，然后求差值
inputList.sort()
fenge = N//2
sum1 = sum(inputList[:fenge])
sum2 = sum(inputList[fenge:])
# print(sum1,sum2)
# print(abs(sum1-sum2))
print(N%2,abs(sum1-sum2))