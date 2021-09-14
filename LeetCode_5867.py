class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            index = word.index(ch)
            res = word[:index+1][::-1]
            res += word[index+1:]
            # print(res)
            return res
        except:
            return word

if __name__ == '__main__':
    # word = "abcdefd"
    # ch = "d"
    word = "abcd"
    ch = "z"
    result = Solution().reversePrefix(word,ch)
    print(result)


