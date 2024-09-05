class Solution:
    def hammingWeight(self, n: int) -> int:
        def tobin(n):
            res=''
            while n>0:
                r = n%2
                res+=str(r)
                n=n//2
            return res[::-1]
        x = tobin(n)
        return x.count('1')
        
