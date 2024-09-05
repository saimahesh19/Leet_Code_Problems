import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return x == x[::-1]
