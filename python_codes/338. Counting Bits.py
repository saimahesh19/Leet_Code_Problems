class Solution:
    def countBits(self, n: int) -> List[int]:
        def b(n):
            b=[]
            while n>0:
                b.append(str(n%2))
                n=n//2
            bs = ''.join(b)
            return bs.count('1')
        k = 0 
        res=[]
        while k<=n:
            res.append(b(k))
            k+=1
        return res 
            

        

        
