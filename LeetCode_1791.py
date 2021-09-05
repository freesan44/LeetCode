class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        resList = []
        #把全部数组拆解出来形成一个List，然后用Counter归纳，找出数量为n的
        for i in edges:
            resList += i
        # print(resList)
        from collections import Counter
        count = Counter(resList)
        for (key, val) in count.items():
            # print(key,val)
            # print(len(edges)-1)
            if val == (len(edges)):
                return key
        return 0

if __name__ == '__main__':
    edges = [[1,2],[2,3],[4,2]]
    ret = Solution().findCenter(edges)
    print(ret)