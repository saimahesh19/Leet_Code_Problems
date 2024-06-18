class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispal(s: str) -> bool:
            return s == s[::-1]

        maxlen = 0
        pal = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if ispal(sub):
                    if len(sub) > maxlen:
                        maxlen = len(sub)
                        pal = sub
        return pal
