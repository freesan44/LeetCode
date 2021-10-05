S1 = list(input())
S2 = list(input())
# S1 = list("They are students.")
# S2 = list("aeiou")
#暴力法
# for i in S2:
#     while True:
#         try:
#             S1.remove(i)
#         except:
#             break
# print("".join(S1))
#字典
S2Dict = dict()
for i in S2:
    S2Dict[i] = 1
res = ""
for j in S1:
    if j not in S2Dict:
        res += j
print(res)