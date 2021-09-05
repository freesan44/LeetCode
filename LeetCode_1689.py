class Solution:
    def minPartitions(self, n: str) -> int:
        return str(max(n))

if __name__ == '__main__':
    n = "32"
    n = "27346209830709182346"
    ret = Solution().minPartitions(n)
    print(ret)