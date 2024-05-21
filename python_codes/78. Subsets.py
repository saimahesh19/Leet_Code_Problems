class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            new_subsets = []
            for current_subset in result:
                new_subset = current_subset + [num]
                new_subsets.append(new_subset)
            result.extend(new_subsets)
        return result
