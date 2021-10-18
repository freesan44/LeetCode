class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) > 0 and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

if __name__ == '__main__':
    s = "abbaca"
    ret = Solution().removeDuplicates(s)
    print(ret)


