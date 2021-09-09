class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # 两个坐标加起来的奇偶性来判断
        one = ord(coordinates[0])-97+1
        two = int(coordinates[1])
        return (one+two)%2 == 1

if __name__ == '__main__':
    coordinates = "a1"
    coordinates = "h3"
    ret = Solution().squareIsWhite(coordinates)
    print(ret)