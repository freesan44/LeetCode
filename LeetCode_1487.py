class Solution:
    def getFolderNames(self, names: [str]) -> [str]:
        ret = []
        nameDict = {}
        for eachStr in names:
            #拆分字符
            import re
            countList = re.findall(r'[(](.*?)[)]', eachStr)
            countList = [int(i) for i in countList]+[0]
            if len(countList) <=0:
                countList = [0]
            name = re.split(r'[(](.*?)[)]',eachStr)[0]
            if name not in nameDict:
                nameDict[name] = [0]
                ret.append(eachStr)
            else:
                nameList = nameDict[name]
                lenCount = len(countList)
                for i in range(lenCount):
                    try:
                        nameList[i] += 1
                    except:
                        nameList.append(0)
                    if i == lenCount-1 :#最后一位
                        if nameList[i] == 0:
                            continue
                        name = name + "(" + str(nameList[i]) + ")"
                        print("2" + " " + str(name))
                    else:
                        name = name + "(" + str(countList[i]) + ")"
                    # name = name + "(" + str(nameList[i]) + ")"
                ret.append(name)
        return ret
if __name__ == '__main__':
    # names = ["gta","gta(1)","gta","avalon"]
    names = ["kaido", "kaido(1)", "kaido", "kaido(1)"]
    ret = Solution().getFolderNames(names)
    print(ret)