class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(" ")
        n = len(words)
        if n == 1:
            return words[0] + " " * spaces
        space_between_words = spaces // (n - 1)
        remainder_spaces = spaces % (n - 1)
        space = " " * space_between_words
        remainder = " " * remainder_spaces
        text = space.join(words) + remainder       
        return text
