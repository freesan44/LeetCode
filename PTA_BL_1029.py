input1Str = input()
input2Str = input()
# input1Str = "7_This_is_a_test"
# input2Str = "hssaes"
# zhizhen1 = 0
# zhizhen2 = 0
# resList = []
# while zhizhen1 < len(input1Str) and zhizhen2 < len(input2Str):
#     char = input1Str[zhizhen1]
#     if char == input2Str[zhizhen2]:
#         zhizhen2 += 1
#     else:#如果不相等，放入结果数组里面
#         if char.isalpha() == True:#字母转成大写
#            char = char.upper()
#         if char not in resList:
#             resList.append(char)
#     zhizhen1 += 1
# print("".join(resList))

input1Str =input1Str.upper()
input2Str =set(input2Str.upper())
resList = []
for i in input1Str:#把所有字符形成唯一数组
    if i not in resList:
        resList.append(i)
for i in input2Str:#删掉重复的
    resList.remove(i)
print("".join(resList))