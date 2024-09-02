class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = list(str(x))
        if str_x == str_x[::-1]:
            return True
        else:
            return False 
        
