class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cou = {}
        for i in nums:
            if i in cou:
                cou[i] += 1
            else:
                cou[i] = 1
        maxi = None
        max_count = 0
        for element, count in cou.items():
            if count > max_count:
                max_count = count
                maxi = element
        return maxi
        
