class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # ##暴力解法，超时
        # answerList = [0]*n
        # for nList in bookings:
        #     first = nList[0]-1
        #     last = nList[1]
        #     seats = nList[2]
        #     for i in range(first, last):
        #         answerList[i] += seats
        # return answerList
        ## 差分数组
        answerList = [0]*n
        for first, last, seats in bookings:
            answerList[first-1] += seats
            if last < n:
                answerList[last] += -seats
            # print(answerList)

        for i in range(1, n):
            answerList[i] += answerList[i-1]
        return answerList


if __name__ == '__main__':
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    ret = Solution().corpFlightBookings(bookings, n)
    print(ret)