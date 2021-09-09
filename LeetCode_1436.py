class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # 用字典形式存储地点
        resDict = dict()
        for iList in paths:
            #如果地点存在，就删除【因为本来就是对数存在】，不存在就添加，并记录是起点还是终点
            for index,val in enumerate(iList):
                if val in resDict:
                    del resDict[val]
                else:
                    resDict[val] = index
        for key,val in resDict.items():
            #val== 1为终点位置
            if val == 1:
                return key




if __name__ == '__main__':
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    ret = Solution().destCity(paths)
    print(ret)