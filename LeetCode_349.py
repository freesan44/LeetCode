class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        # res = []
        # nums1 = list(set(nums1))
        # nums2 = list(set(nums2))
        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1
        # for i in nums1:
        #     if i in nums2:
        #         res.append(i)
        # # res = list(set(res))
        # return res
        #用纯元组与&实现
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    ret = Solution().intersection(nums1,nums2)
    print(ret)