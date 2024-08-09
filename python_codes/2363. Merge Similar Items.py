class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        x = {item[0]: item[1] for item in items1}
        y = {item[0]: item[1] for item in items2}
        result = {}
        for key, value in x.items():
            result[key] = value
        for key, value in y.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
        sorted_result = sorted(result.items())
        final_result = [[key, value] for key, value in sorted_result]
        return final_result
