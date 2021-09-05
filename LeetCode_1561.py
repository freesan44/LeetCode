class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # 其实是获取从大到小每隔一个的值，直到遍历2/3停止
        piles.sort(reverse=True)
        res = 0
        for i in range(1,(len(piles)*2)//3,2):
            # print(i)
            res += piles[i]
        return res


if __name__ == '__main__':
    piles = [9,8,7,6,5,1,2,3,4]
    ret = Solution().maxCoins(piles)
    print(ret)