class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_vowels = 0
        vol = 0
        for i in range(k):
            if s[i] in vowels:
                vol += 1
        max_vowels = vol
        for i in range(k, len(s)):
            if s[i] in vowels:
                vol += 1
            if s[i - k] in vowels:
                vol -= 1
            max_vowels = max(max_vowels, vol)
        return max_vowels
