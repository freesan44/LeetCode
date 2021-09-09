class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 用Counter或者Set，如果==26个字母就True
        from collections import Counter
        count = Counter(sentence)
        # count = set(sentence)
        if len(count) == 26:
            return True
        else:
            return False


if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    sentence = "leetcode"
    ret = Solution().checkIfPangram(sentence)
    print(ret)