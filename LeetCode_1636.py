class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        from collections import Counter
        # most_common，在Counter中按照数量排序
        counter = Counter(nums).most_common()
        print(counter)
        # 排序，优先数量，次优先反序字母
        counter.sort(key=lambda x: (x[1], -x[0]))
        # print(counter)
        # 添加输出
        for val,count in counter:
            res += [val] * count
            # for _ in range(count):
            #     res.append(val)
        # res.reverse()
        return res


if __name__ == '__main__':
    # nums = [1,1,2,2,2,3]
    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    # nums = [2, 3, 1, 3, 2]
    # nums = [1,5,0,5]
    ret = Solution().frequencySort(nums)
    print(ret)