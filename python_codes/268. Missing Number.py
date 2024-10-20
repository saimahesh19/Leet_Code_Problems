
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = sorted(nums)  # Sort the list
        num_set = set(n)  # Create a set from the sorted list for O(1) lookups

        for i in range(len(n) + 1):  # Check from 0 to n
            if i not in num_set:  # If the number is not in the set, return it
                return i
        
        return n[-1] + 1  # This line won't be reached, but it handles the case when all numbers are present
