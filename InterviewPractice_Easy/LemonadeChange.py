class Solution:

    # brute force, very slow.
    def lemonadeChange(self, bills: List[int]) -> bool:
        dbills = {5: 0, 10: 0, 20: 0}

        for i in bills:
            dbills[i] += 1

            if i != 5:
                change = i - 5
                print(dbills)
                for j in sorted(dbills.keys(), reverse=True):
                    while dbills[j] > 0 and change // j > 0:
                        change -= j
                        dbills[j] -= 1
                        print("bill: ", j, "chage: ", change)

                if change != 0:
                    return False

        return True

    """ 
    reflection: 
    Thought more about: 
    - 저장될 변수들의 범위. (range of the variables to be saved - quite narrow - 5, 10, 20, 15)
    - we don't need to keep dictionary dbills, we can use integer variables to keep track of the count of 5, 10 bills (20 disregard) 
    - the change is always going to be between 5-15 (10, 20 bill)
    """

    def lemonadeChange_V2(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for i in bills:
            if i == 5:
                five += 1

            # where we need to provide change.
            elif i == 10:
                ten += 1

                if five > 0:
                    five -= 1
                else:
                    return False

            # for 20 bills
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1

                elif ten == 0 and five > 2:
                    five -= 3
                else:
                    return False

        return True

    # Sample fastest solution
    def lemonadeChange_V3(self, bills: List[int]) -> bool:
        five = ten = twenty = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five == 0:
                    return False
                ten += 1
                five -= 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
                twenty += 1

        return True
