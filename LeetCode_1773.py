class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        type = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        index = type[ruleKey]
        resList = [i[index] for i in items]

        return resList.count(ruleValue)

if __name__ == '__main__':
    # items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
    #          ["phone", "gold", "iphone"]]
    # ruleKey = "color"
    # ruleValue = "silver"
    items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"],
             ["phone", "gold", "iphone"]]
    ruleKey = "type"
    ruleValue = "phone"
    ret = Solution().countMatches(items, ruleKey, ruleValue)
    print(ret)