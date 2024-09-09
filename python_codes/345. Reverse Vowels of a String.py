class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set('aeiouAEIOU')
        i =0 
        j  =len(s)-1
        s1 = list(s)
        while i<j:
            if s1[i] not in v:
                i+=1
                continue
            if s1[j] not in v:
                j-=1
                continue
            s1[i],s1[j]=s1[j],s1[i]
            i+=1
            j-=1
        return ''.join(s1)
        
        
