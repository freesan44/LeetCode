N, C = map(str, input().split())
# N, C = map(str, "10 a".split())
N = int(N)
print(C*N)
h = int(N/2+0.5)-2 #+0.5再转int为四舍五入
for _ in range(h):
    print(C + " "*(N-2) + C)
print(C*N)