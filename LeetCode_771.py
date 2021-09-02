class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        counter = Counter(stones)
        res = 0
        for i in jewels:
            res += counter.get(i, 0)
        # print(Counter(stones))
        return res


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    result = Solution().numJewelsInStones(J, S)
    print(result)
