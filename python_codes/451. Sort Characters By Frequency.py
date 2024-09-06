class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        items = list(freq.items())
        n = len(items)
        for i in range(0,n):
            for j in range(0,n-i-1):
                if items[j][1]<items[j+1][1]:
                    items[j], items[j+1] = items[j+1], items[j]
        res=''
        for i, j in items:
            res+=i*j
        return res

        
        
