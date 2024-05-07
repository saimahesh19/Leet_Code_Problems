class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []] 
        for num1 in nums1:
            if num1 not in nums2 and num1 not in answer[0]:
                answer[0].append(num1)
        for num2 in nums2:
            if num2 not in nums1 and num2 not in answer[1]:
                answer[1].append(num2)
        return answer
