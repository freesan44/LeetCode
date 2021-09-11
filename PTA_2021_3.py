inputStr = input()
# inputStr = "This is apintiatest. Hey I love pintia, really zhen ai pintia la,pintia is my favorite place to go. Come on visit Pintia."
# inputStr = "This is apintia test. Hey I love pintia a"
# inputStr = ".pintia."

length = len(inputStr)
res = 0
testStr1 = "pintia"
testStr2 = "Pintia"
for i in range(0, length-len(testStr1)+1):
    test = inputStr[i:i+len(testStr1)]
    if test== testStr1 or test== testStr2:
        leftStr = " " if i==0 else inputStr[i-1]
        # print(inputStr[i+len(testStr1)])
        rightStr = " " if i+len(testStr1) == length else inputStr[i+len(testStr1)]
        if leftStr.isalpha() == False and rightStr.isalpha() == False:
            res += 1
print(res)
if res == 0:
    print("wu gan")
elif res <= 3:
    print("you ai")
else:
    print("zhen ai la")