class Solution:
    def compress(self, chars: List[str]) -> int:
        temp = 1
        r = []
        
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                temp += 1
            else:
                r.append(chars[i - 1])
                if temp > 1:
                    r.extend(list(str(temp)))
                temp = 1

        chars[:] = r  
        return len(chars)
