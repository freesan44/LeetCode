N = int(input())
# N = int(5)
for _ in range(N):
    inputStr = str(input())
    # inputStr = str("pass*word.6")
    # print(inputStr.isnumeric())
    # print(len(inputStr))

    if len(inputStr)<6:
        print("Your password is tai duan le.")
        continue
    hasZimu = False
    hasShuzi = False
    hasBuhefazimu = False
    for i in inputStr:
        if i.isalpha():
            hasZimu = True
        if i.isnumeric():
            hasShuzi = True
        if i.isalpha() == False and i.isnumeric() == False and i != ".":
            hasBuhefazimu = True
    if hasBuhefazimu:
        print("Your password is tai luan le.")
        continue
    if hasZimu == True and hasShuzi == False:
        print("Your password needs shu zi.")
    elif hasZimu == False and hasShuzi == True:
        print("Your password needs zi mu.")
    elif hasZimu == True and hasShuzi == True:
        print("Your password is wan mei.")