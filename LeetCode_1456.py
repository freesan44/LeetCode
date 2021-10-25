class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        coreDic = dict()
        coreDic = {"a":1,"e":1,"i":1,"o":1,"u":1}
        res,temp = 0,0
        #先形成k那样的滑动窗口
        for i in s[:k]:
            if i in coreDic:
                temp += 1
        if len(s) == k : return temp
        res = temp
        #开始滑动窗口，把旧的-1，新的+1
        for index,val in enumerate(s[k:]):
            if s[index] in coreDic:
                temp -= 1
            if val in coreDic:
                temp += 1
            res = max(temp,res)
        return res

if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    result = Solution().maxVowels(s,k)
    print(result)