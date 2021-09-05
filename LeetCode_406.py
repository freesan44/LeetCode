class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key= lambda x:(-x[0],x[1]))
        # print(people)
        # 在本题目中，我首先对数对进行排序，按照数对的元素 1 降序排序，按照数对的元素 2 升序排序。原因是，按照元素 1 进行降序排序，对于每个元素，在其之前的元素的个数，就是大于等于他的元素的数量，而按照第二个元素正向排序，我们希望 k 大的尽量在后面，减少插入操作的次数。
        resList = []
        for p in people:
            if len(resList) <= p[1]:
                resList.append(p)
            elif len(resList) > p[1]:
                resList.insert(p[1], p)
            # print(resList)
        return resList
if __name__ == '__main__':
    people = [[4,4],[7,1],[5,0],[7,0],[6,1],[5,2]]
    # people = [[5,0],[6,0],[4,0],[3,2],[2,2],[1,4]]
    ret = Solution().reconstructQueue(people)
    print(ret)