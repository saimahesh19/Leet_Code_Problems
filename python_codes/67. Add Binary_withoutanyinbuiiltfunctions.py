class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = list(a)
        d = list(b)
        inta = 0
        intb = 0
        for i in range(len(c)):
            inta += (2 ** (len(c) - 1 - i)) * int(c[i])
        for i in range(len(d)):
            intb += (2 ** (len(d) - 1 - i)) * int(d[i])
        total_sum = inta + intb
        res = []
        if total_sum == 0:
            return "0"
        while total_sum > 0:
            res.append(str(total_sum % 2))
            total_sum = total_sum // 2
        res.reverse()
        return ''.join(res)
