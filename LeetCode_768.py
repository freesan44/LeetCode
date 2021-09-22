class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for i in arr:
            if stack and stack[-1]>i:
                cur = stack[-1]
                while stack and stack[-1]>i:
                    stack.pop()
                stack.append(cur)
            else:
                stack.append(i)
        return len(stack)



if __name__ == '__main__':
    arr = [5,4,3,2,1]
    result = Solution().maxChunksToSorted(arr)
    print(result)


