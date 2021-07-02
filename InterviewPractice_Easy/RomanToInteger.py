class Solution:
    def romanToInt(self, s: str) -> int:
        # "IV": 4, "IX": 9, "XL": 50, "XC": 90, "CD": 400, "CM": 900
        conversion = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }

        total = 0

        first, second = 0, 1

        i = 0

        while(i < len(s)):
            if i+1 < len(s) and conversion[s[i]] < conversion[s[i+1]]:
                total += conversion[s[i+1]] - conversion[s[i]]
                i += 2
            else:
                total += conversion[s[i]]
                i += 1

        return(total)

    def romanToInt(self, s: str) -> int:
