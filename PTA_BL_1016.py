A, Da, B, Db = map(str, input().split())
# A, Da, B, Db = map(str, "3862767 6 13530293 3".split())
PaStr = "0"#用0方便边界条件
PbStr = "0"
for i in list(A):
    if i == Da:
        PaStr += i
for i in list(B):
    if i == Db:
        PbStr += i
print(str(int(PaStr)+int(PbStr)))