A, B, D = map(int, input().split())
# A, B, D = map(int, "123 456 8".split())
num = A + B
isFushu = False
if num < 0:#处理负数的问题
    isFushu = True
num = abs(num)
res = ""
while num != 0:
    r = num % D  #求余得到的数为尾数
    num = num//D  #取除数进位
    res = str(r)+res
if isFushu == True:res = "-"+res
if len(res) == 0:#添加边界条件
    print("0")
else:
    print(res)
