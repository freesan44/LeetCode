class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        # #nums1为短数组
        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1
        # lenN1 = len(nums1)
        # lenN2 = len(nums2)
        # res = []
        # for i in range(lenN1):
        #     if nums1[i] in nums2:
        #         res.append(nums1[i])
        #         nums2.pop(nums2.index(nums1[i]))
        # return res
        #排序求交集
        # nums1为短数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1.sort()
        nums2.sort()
        lenN1 = len(nums1)
        lenN2 = len(nums2)
        res = []
        p = 0
        q = 0
        while p < lenN1 and q < lenN2:
            if nums1[p] == nums2[q]:
                res.append(nums1[p])
                p += 1
                q += 1
            elif nums1[p] > nums2[q]:
                q += 1
            else:
                p += 1
        return res

if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    # nums1 = [1, 2]
    # nums2 = [1, 1]
    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]
    res = Solution().intersect(nums1,nums2)
    print(res)