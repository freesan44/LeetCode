input1List = input().split(" ")
# input1List = "5000 7000".split(" ")
num1 = int(input1List[0])
num2 = int(input1List[1])
res = str(num1*num2)
# 把000之类的去掉
resRe = int(res[::-1])
print(resRe)
