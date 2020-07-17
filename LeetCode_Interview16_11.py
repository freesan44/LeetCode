class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> [int]:
        if k <=0:return []#边界条件
        ret = [shorter*(k-i)+longer*i for i in range(k+1)]
        if shorter == longer:#边界条件，长短相同
            return list(set(ret))
        return ret


if __name__ == '__main__':
    shorter = 2
    longer = 2
    k = 3
    result = Solution().divingBoard(shorter, longer, k)
    print(result)