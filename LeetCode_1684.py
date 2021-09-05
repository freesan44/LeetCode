class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        ## 通过Set方式来进行判断抽取，复杂度降低
        allowedSet = set(allowed)
        for word in words:
            wordSet = set(word)
            if wordSet.issubset(allowedSet):
                res += 1
            # res += 1
            # for i in wordSet:
            #     if i not in allowedSet:
            #         res -= 1
            #         break
        return res

if __name__ == '__main__':
    # allowed = "ab"
    # words = ["ad","bd","aaab","baa","badab"]
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    ret = Solution().countConsistentStrings(allowed, words)
    print(ret)