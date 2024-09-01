class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxi = 0
        count = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                count += 1
            else:
                maxi = max(maxi, count)
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                    count -= 1
                left += 1  
            maxi = max(maxi, count)
        return maxi
