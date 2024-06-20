
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        
        merged_intervals = [intervals[0]]
        
        for current in intervals[1:]:
            previous = merged_intervals[-1]
            
            if current[0] <= previous[1]: 
                previous[1] = max(previous[1], current[1])
            else:
                merged_intervals.append(current)
        
        return merged_intervals
