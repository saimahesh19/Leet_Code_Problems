class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum1 = [0] 
        for i in range(len(gain)):
            sum1.append(sum1[-1] + gain[i]) 
        high_alt = max(sum1)
        return high_alt
