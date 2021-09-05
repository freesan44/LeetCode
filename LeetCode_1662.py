class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # 用join，把list转成str
        word1Str = "".join(word1)
        word2Str = "".join(word2)
        return word1Str == word2Str


if __name__ == '__main__':
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    ret = Solution().arrayStringsAreEqual(word1, word2)
    print(ret)