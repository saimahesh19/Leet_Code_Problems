class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        items = list(freq.items())
        n= len(items)
        for i in range(0,n):
            for j in range(0, n-i-1):
                if items[j][1]<items[j+1][1]:
                    items[j],items[j+1]=items[j+1],items[j]
        res=[]
        for i in range(0,k):
            res.append(items[i][0])
        return res

        
