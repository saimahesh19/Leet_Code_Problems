class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        rev = s[::-1]  
        res = []
        for i in range(n):  
            if rev[i] != " ":
                res.append(rev[i])
            elif rev[i] == " " and res:
                break
        return len(res)
