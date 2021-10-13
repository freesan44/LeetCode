class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        sh,sm = map(int,startTime.split(":"))
        eh,em = map(int,finishTime.split(":"))
        # 转成分钟后判断
        sSum = sh*60 + sm
        eSum = eh*60 + em
        # 第二天
        if eSum < sSum:
            eSum += 24*60
        # 开始时间向上取整，结束时间向下取整
        sCount = sSum//15 + (1 if sSum%15 >0 else 0)
        eCount = eSum//15
        return max(0,eCount-sCount)





if __name__ == '__main__':
    startTime = "00:00"
    finishTime = "23:59"
    startTime = "12:01"
    finishTime = "12:44"
    startTime = "20:00"
    finishTime = "06:00"
    ret = Solution().numberOfRounds(startTime,finishTime)
    print(ret)