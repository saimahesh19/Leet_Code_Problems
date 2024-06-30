class Solution:
    def lastRemaining(self, n: int) -> int:
        a = list(range(1, n + 1))  # Include 'n' in the range
        
        def removealt(arr):
            return arr[1::2]  # Remove every other element
        
        def removeleft(arr):
            if len(arr) > 1:
                return removealt(arr)
            else:
                return arr
        
        def removeright(arr):
            if len(arr) > 1:
                arr = arr[::-1]  # Reverse the array
                arr = removealt(arr)
                arr = arr[::-1]  # Reverse back to original order after removal
                return arr
            else:
                return arr
        
        while len(a) > 1:
            a = removeleft(a)
            a = removeright(a)
        
        return a[0]



//optimised code 
class Solution:
    def lastRemaining(self, n: int) -> int:
      left_to_right = True
      step = 1
      remaining = n
      head = 1
      
      while remaining > 1:
          if left_to_right or remaining % 2 == 1:
              head += step
          
          remaining //= 2
          step *= 2
          left_to_right = not left_to_right
      
      return head
