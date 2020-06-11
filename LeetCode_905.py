class Solution:
    def sortArrayByParity(self, A: [int]) -> [int]:
        # #双指针
        # left = 0
        # right = len(A)-1
        # while left != right:
        #     if A[left] %2 == 0:
        #         left += 1
        #         continue
        #     if A[right] %2 == 1:
        #         right -= 1
        #         continue
        #     A[left], A[right] = A[right], A[left]
        #     left += 1
        #     if left == right:break
        #     right -= 1
        # return A
        #数组
        ret = []
        for i in A:
            if i %2 == 0:
                ret.insert(0,i)
            else:
                ret.append(i)
        return ret

if __name__ == '__main__':
    nums = [3,1,2,4]
    ret = Solution().sortArrayByParity(nums)
    print(ret)