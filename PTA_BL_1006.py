count = int(input())
# count = 234
outPutStr = ""
# 处理百位
baiweiCount = count//100
for i in range (baiweiCount):
    outPutStr = outPutStr + "B"
# 处理十位
shiweiCount = (count % 100)//10
for j in range(shiweiCount):
    outPutStr = outPutStr + "S"
# 处理个位
geweiCount = count%10
for k in range(1,geweiCount+1):
    outPutStr = outPutStr + str(k)
print(outPutStr)