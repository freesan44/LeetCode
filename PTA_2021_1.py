L,a,b,f = map(str,input().split())
# L,a,b,f = map(str,"6 a b -".split())
L = int(L)

for i in range(L):
    left = i
    right = L-i-1
    mid = i+1
    print(b*left + f + a*right)