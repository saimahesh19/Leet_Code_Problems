class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str3 = ""
        min_len = min(len(word1), len(word2))
        
        for i in range(min_len):
            str3 += word1[i] + word2[i]
        
        # Add the remaining characters from the longer word
        str3 += word1[min_len:] + word2[min_len:]
        
        return str3
