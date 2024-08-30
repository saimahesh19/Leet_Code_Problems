class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(rem, combo,start):
            if rem==0:
                return result.append(list(combo))
            elif rem<0:
                return
            for i in range(start,len(candidates)):
                combo.append(candidates[i])
                backtrack(rem-candidates[i],combo, i)
                combo.pop()
        result=[]
        backtrack(target, [],0)
        return result

        
