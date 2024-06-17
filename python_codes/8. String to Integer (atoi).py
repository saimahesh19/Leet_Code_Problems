class Solution:
    def myAtoi(self, s: str) -> int:
        nums = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        s = s.strip() 
        if not s:
            return 0
        res = []
        sign = 1
        start = 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        for i in range(start, len(s)):
            if s[i] not in nums:
                break
            res.append(s[i])
        if not res:
            return 0
        result_str = ''.join(res)
        result = int(result_str) * sign
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max
        return result
