class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbol=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        roman_numerical =''
        i=0
        while num>0:
            for _ in range(num//val[i]):
                roman_numerical +=symbol[i]
                num-=val[i]
            i+=1
        return roman_numerical


        
