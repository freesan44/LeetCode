N,D = map(int, input().split())
# N,D = map(int, "3 20".split())
kuCunList = list(map(float, input().split()))
# kuCunList = list(map(int, "18 15 10".split()))
# kuCunList = list(map(int, "1".split()))
shoujiaList = list(map(float, input().split()))
# shoujiaList = list(map(int, "75 72 45".split()))
# shoujiaList = list(map(int, "1".split()))
zipList = list(zip(kuCunList, shoujiaList))
##if len(zipList) <= 0 or N == 0 or D ==0:
##    print("%.2f" % 0)
# 压缩数组
zipList = [(x,y,y/x) for (x,y) in zipList]
zipList.sort(key= lambda x: -x[2])

res = 0
for x,y,z in zipList:
    # print(x,y,z)
    if D == 0:
        break
    if D-x >= 0:
        res += y
        D -= x
    else:
        res += D * z
        D = 0
    # print(D)
# while D != 0:
#     try:
#         x,y,z = zipList.pop()
#     except:
#         break
#     if D-x >= 0:
#         res += y
#         D -= x
#     else:
#         res += D*z
#         D = 0
#     # print(zipList)
print("%.2f" % res)#保留小数点两位