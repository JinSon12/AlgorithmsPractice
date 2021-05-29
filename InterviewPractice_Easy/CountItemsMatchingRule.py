# Count Items Matching a Rule

# 1st try.
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        itemContainer = {}
        count = 0
        ruleInd = 0

        if ruleKey == "type":
            ruleInd = 0
        elif ruleKey == "color":
            ruleInd = 1
        else:
            ruleInd = 2

        for i in range(0, len(items)):
            itemContainer[i] = items[i]

        for item in itemContainer:
            if ruleValue == itemContainer[item][ruleInd]:
                count += 1

        return count
