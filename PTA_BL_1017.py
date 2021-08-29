A, B = map(int, input().split())
# A, B = map(int, "123456789050987654321 7".split())
# 不正规的解法
# print(str(A//B)+ " " + str(A%B))
# 正规解法
A = str(A)
res = ""
next = "0"
for i in range(len(A)):
    res = res + str(int(next + A[i])//B) #从上一位的next加到当前位再除
    next = str(int(next + A[i]) % B)
print(int(res), next)
