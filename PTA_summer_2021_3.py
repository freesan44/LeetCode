start = input()
target = input()
N = int(input())
# start = "This is a test."
# target = "Tom is a cat."
# N = int("1")

for _ in range(N):
    actionNum = int(input())
    testStr = list(input())
    # actionNum = int("6")
    # testStr = list("0 2 2 1 000000 1 2 2 00")
    left = 0
    right = 0#对的数组index
    res = ""
    while len(testStr)!=0:
        s = testStr.pop(0)
        if s == "0":
            res += start[left]
            left += 1
            right += 1
        elif s == "1":
            # print(start[left])
            left += 1
            # print(start[left])
            actionNum -= 1
        elif s == "2":
            res += target[right]
            left += 1
            right += 1
            actionNum -= 1
        elif s == "3":
            res += target[right]
            right += 1
            actionNum -= 1
        else:
            actionNum = -1
        # print(left,right)
        # print(s,res)
    # print(res)
    if res == target and actionNum == 0:
        print("AC")
    else:
        print("WA")