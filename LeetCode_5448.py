class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pathList = list(path)
        stepList = ["0 0"]
        while len(pathList)>0:
            # print(stepList)
            step = pathList.pop(0)
            lastStep = stepList[-1]
            tempList = lastStep.split(" ")
            x = int(tempList[0])
            y = int(tempList[1])
            if step == "N":
                y = y +1
            elif step == "S":
                y = y - 1
            elif step == "E":
                x = x + 1
            elif step == "W":
                x = x - 1
            newStepStr = str(x) + " " + str(y)
            if newStepStr in stepList:
                return True
            stepList.append(newStepStr)
        return False


if __name__ == '__main__':
    path = "NES"
    path = "NESWW"
    ret = Solution().isPathCrossing(path)
    print(ret)
