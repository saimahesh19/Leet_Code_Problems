class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        prefix = ""
        for j in range(len(strs[0])):
            prefix += strs[0][j]  
            common = True 
            for i in range(1, len(strs)):
                if not strs[i].startswith(prefix):
                    common = False
                    break  
            if common:
                res.append(prefix[-1])
            else:
                break 
        return ''.join(res)
