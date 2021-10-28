class Solution:
    def minTimeToType(self, word: str) -> int:
        temp = "a"
        tempStap = ord(temp)
        res = 0
        for i in word:
            target = ord(i)
            res += min(26-abs(target-tempStap),abs(target-tempStap))+1
            # print(res,tempStap,target)
            tempStap = target
        return res

if __name__ == '__main__':
    word = "bza"
    res = Solution().minTimeToType(word)
    print(res)