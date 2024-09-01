class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        res = []
        if x_str[0] == '-':
            res.append('-')
            res.extend(x_str[1:][::-1])
        else:
            res.extend(x_str[::-1])  
        reversed_number = int(''.join(res))
        if reversed_number < -2**31 or reversed_number > 2**31 - 1:
            return 0
        return reversed_number
