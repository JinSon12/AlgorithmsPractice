class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
            "IV": 4, "IX": 9, "XL": 50, "XC": 90, ""
        }

        print(conversion["I"])

    def romanToInt(self, s: str) -> int:
