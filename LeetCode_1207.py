class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        counter = Counter(arr)
        setCounter = set(counter.values())
        return len(setCounter) == len(counter.values())

if __name__ == '__main__':
    arr = [1,2,2,1,1,3]
    arr = [1, 2]
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    ret = Solution().uniqueOccurrences(arr)
    print(ret)