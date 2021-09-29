class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums).most_common(k)
        # print([key for key,val in counter])
        return [key for key,val in counter]
if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    ret = Solution().topKFrequent(nums, k)
    print(ret)