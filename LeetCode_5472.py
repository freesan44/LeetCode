class Solution:
    def restoreString(self, s: str, indices: [int]) -> str:
        tempList = [""]*len(indices)
        strList = list(s)
        for idx,val in enumerate(indices):
            tempStr = strList[idx]
            tempList[val] = tempStr
        # print(tempList)
        return "".join(tempList)
if __name__ == '__main__':
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    result = Solution().restoreString(s, indices)
    print(result)