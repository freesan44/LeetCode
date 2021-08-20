str = input()
# str = "Hello World Here I Come"
# 字符串数组
strList = str.split(" ")
# 倒序
strList.reverse()
res = " ".join(strList)
print(res)