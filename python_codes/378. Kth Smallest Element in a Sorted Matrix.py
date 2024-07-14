class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flattened = []
        for row in matrix:
            flattened.extend(row)
        flattened.sort()
        return flattened[k - 1]
