class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i%3 ==0 and i%5 == 0:#同时被3、5整除
                res.append("FizzBuzz")
            elif i%3 ==0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
if __name__ == '__main__':
    n = 15
    ret = Solution().fizzBuzz(n)
    print(ret)