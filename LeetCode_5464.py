class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret = numBottles
        cache = numBottles
        while cache >= numExchange:
            eachExchange = cache//numExchange
            ret = ret + eachExchange
            cache = eachExchange + cache%numExchange
        return ret



if __name__ == '__main__':
    numBottles = 2
    numExchange = 3
    result = Solution().numWaterBottles(numBottles, numExchange)
    print(result)