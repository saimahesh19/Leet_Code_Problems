class Solution:
    def romanToInt(self, s: str) -> int:
        roman_symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,}
        sum = 0
        prev_self = 0
        for self in reversed(s):
             if prev_self > roman_symbol[self]:
                sum -= roman_symbol[self]
             else:
                sum += roman_symbol[self]
                prev_self = roman_symbol[self]
        return sum                   
