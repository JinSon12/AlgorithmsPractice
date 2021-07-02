class Solution:
    def romanToInt(self, s: str) -> int:
        # "IV": 4, "IX": 9, "XL": 50, "XC": 90, "CD": 400, "CM": 900
        conversion = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }

        total = 0

        first, second = 0, 1

        i = 1

        while(i < len(s)):
            print(i, "i")
            print(total)
            if conversion[s[i-1]] < conversion[s[i]]:
                print(s[i-1], s[i])
                total += conversion[s[i]] - conversion[s[i-1]]
                i += 2
                print(total)
            else:
                print(s[i-1])
                total += conversion[s[i-1]]
                i += 1

        return(total)

    def romanToInt(self, s: str) -> int:
