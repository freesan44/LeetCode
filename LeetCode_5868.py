class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        from collections import defaultdict
        resDict = defaultdict(list)
        from fractions import Fraction
        for arr in rectangles:
            x,y = arr[0],arr[1]
            fa = Fraction(x,y)
            resDict[(fa.numerator,fa.denominator)].append(arr)
        res = 0
        for key,val in resDict.items():
            length = len(val)
            if length >=2:
                res+= (length*(length-1))//2
        return res


if __name__ == '__main__':
    rectangles = [[4,8],[3,6],[10,20],[15,30]]
    result = Solution().interchangeableRectangles(rectangles)
    print(result)


