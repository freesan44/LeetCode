class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1List = list(map(int,version1.split(".")))##转成[int]数组 ，可以不转数组然后根据char逐个遍历
        v2List = list(map(int,version2.split(".")))##转成[int]数组 ，可以不转数组然后根据char逐个遍历
        for i in range(len(v1List) if len(v1List)>len(v2List) else len(v2List)):
            v1Val = 0
            v2Val = 0
            if i <= len(v1List)-1:
                v1Val = v1List[i]
            if i <= len(v2List)-1:
                v2Val = v2List[i]
            if v1Val == v2Val:
                continue
            elif v1Val > v2Val:
                return 1
            else:
                return -1
        return 0

if __name__ == '__main__':
    version2 = "1.0.1"
    version1 = "1"
    result = Solution().compareVersion(version1, version2)
    print(result)