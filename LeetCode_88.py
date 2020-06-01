class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-m):
            nums1.pop()
        for j in range(n):
            nums1.append(nums2[j])
        nums1.sort()




if __name__ == '__main__':
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution().merge(nums1, m, nums2, n)
    print(nums1)