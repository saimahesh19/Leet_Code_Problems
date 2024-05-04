class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into a list of words
        words = s.split()
        
        # Reverse the order of words
        reversed_words = words[::-1]
        
        # Join the reversed words back into a single string
        reversed_sentence = ' '.join(reversed_words)
        
        return reversed_sentence
