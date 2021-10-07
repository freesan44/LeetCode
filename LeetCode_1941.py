class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        counter = Counter(s)
        counterVal = Counter(counter.values())
        return len(counterVal) == 1



if __name__ == '__main__':
    s = "abacbc"
    s = "aaabb"
    ret = Solution().areOccurrencesEqual(s)
    print(ret)