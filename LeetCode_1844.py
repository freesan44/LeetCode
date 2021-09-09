class Solution:
    def replaceDigits(self, s: str) -> str:
        # 转成数组方便修改
        sList = list(s)
        for index, val in enumerate(sList):
            val = str(val)
            if val.isnumeric():
                # ord:把字符转成ASCII对应值， chr:转回来
                c = chr(ord(sList[index-1])+int(val))
                sList[index] = c
        return "".join(sList)


if __name__ == '__main__':
    s = "a1c1e1"
    ret = Solution().replaceDigits(s)
    print(ret)