class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = [1,2,4,8,0,0,0,0,0,0]
        minutes = [0,0,0,0,1,2,4,8,16,32]
        res = set()
        #通过枚举遍历有可能出现的可能性
        def possible_number(remindNums,index,hour,minute):
            if hour >11 or minute > 59:
                return
            if remindNums == 0:
                resStr = "%d:%02d"% (hour,minute)
                res.add(resStr)
                return
            for i in range(index,10):
                # print("i",i)
                possible_number(remindNums-1,i+1,hour + hours[i],minute+minutes[i])
        possible_number(turnedOn,0,0,0)
        return list(res)

if __name__ == '__main__':
    # turnedOn = 1
    turnedOn = 2
    res = Solution().readBinaryWatch(turnedOn)
    print(res)