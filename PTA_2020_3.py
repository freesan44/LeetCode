N, D = map(int,input().split())
# N, D = map(int, "7 3".split())

for _ in range(N):
    type, inpStr = map(str, input().split())
    # type, inpStr = map(str, "3 3.14150".split())
    if type == "2":
        index = list(inpStr).index(".")+1
        try:
            # 补0
            if len(inpStr) < index + D:
                inpStr += "0" * (index + D - len(inpStr))
            print(inpStr[:index+D])
        except:
            # 补0
            if len(inpStr) < index + D:
                inpStr += "0" * (index + D - len(inpStr))
            print(inpStr)
    elif type == "1":
        inpStrList = list(inpStr)
        index = inpStrList.index(".")+1
        try:
            res = float(inpStr[:index + D])  # 输出结果
            sishewuru = int(inpStrList[index+D])
            if sishewuru >= 5:
                jiawei = float("0."+"0"*index+"1")
                res += jiawei
            print(res)
        except:
            # 补0
            if len(inpStr) < index + D:
                inpStr += "0" * (index + D - len(inpStr))
            print(inpStr)

    elif type == "3":
        inpStrList = list(inpStr)
        index = inpStrList.index(".") + 1
        try:
            sishewuru = int(inpStrList[index + D])
            res = float(inpStr[:index + D])  # 输出结果
            if sishewuru > 5:
                jiawei = float("0." + "0" * index + "1")
                res += jiawei
            elif sishewuru == 5:
                sishewuruhou = int(inpStrList[index + D+1])
                if sishewuruhou != None and sishewuruhou == 0:
                    #则当有效位最后一位是单数时进位，双数时舍去，即保持最后一位是双数。
                    houyiwei = int(inpStrList[index + D-1])
                    if houyiwei%2 == 1:
                        jiawei = float("0." + "0" * index + "1")
                        res += jiawei
                elif sishewuruhou != None and sishewuruhou != 0:
                    jiawei = float("0." + "0" * index + "1")
                    res += jiawei
            print(res)
        except:
            #补0
            if len(inpStr) < index+D:
                inpStr += "0"*(index+D-len(inpStr))
            print(inpStr)