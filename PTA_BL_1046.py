inputRound = int(input())
# inputRound = 5
aWin = 0
bWin = 0
for i in range(inputRound):
    aH,aNum,bH,bNum = map(int, input().split())
    # aH, aNum, bH, bNum = map(int, "3 8 5 12".split())
    if aNum != bNum:
        if aNum == (aH + bH):
            aWin += 1
        elif bNum == (aH + bH):
            bWin += 1
print(str(bWin)+ " " + str(aWin))
