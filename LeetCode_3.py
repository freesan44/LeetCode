class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        resMax = 0
        hashSet = set()
        # 通过双指针和set检测是否有相同元素，有就左移set
        while right < len(s):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[right])
            resMax = max(resMax, len(hashSet))
            # print(hashSet)
            right += 1
        return resMax
if __name__ == '__main__':
    # s = "pwwkew"
    # s = " "
    s = "dvdf"
    ret = Solution().lengthOfLongestSubstring(s)
    print(ret)