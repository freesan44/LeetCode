C1, C2 = map(int, input().split())
# C1, C2 = map(int, "123 4572973".split())
second = (C2 - C1)/100
h = "%02d" % int(second//3600) #【"%02d" %w】为格式化操作
m = "%02d" % int(second%3600//60)
s = "%02d" % int(second%60+0.5) #+0.5是为了四舍五入
print(h+":"+m+":"+s)
