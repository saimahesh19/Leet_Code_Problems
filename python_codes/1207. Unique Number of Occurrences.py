class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence_count = {}
        for num in arr:
            if num in occurrence_count:
                occurrence_count[num] += 1
            else:
                occurrence_count[num] = 1
        count_set = set()
        for count in occurrence_count.values():
            if count in count_set:
                return False
            else:
                count_set.add(count)
        return True
