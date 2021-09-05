class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 按相反顺序处理，先pop最后那个放最前面，然后加入deck的第一位，
        deck.sort()
        res = [deck.pop()]
        while len(deck) != 0:
            res.append(res.pop(0))
            res.append(deck.pop())
        return res[::-1]


if __name__ == '__main__':
    deck = [17,13,11,2,3,5,7]
    ret = Solution().deckRevealedIncreasing(deck)
    print(ret)