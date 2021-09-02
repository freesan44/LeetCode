class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # res = 0
        # for arr in accounts:
        #     max = sum(arr)
        #     if max > res:
        #         res = max
        # return res
        # 一行实现
        # return max(sum(i) for i in accounts)
        return max(sum(accounts[i]) for i in range(len(accounts)))


if __name__ == '__main__':
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    ret = Solution().maximumWealth(accounts)
    print(ret)