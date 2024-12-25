class Solution:
    def evalPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens[::-1]:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
            if i =='+':
                stack.append(a+b)
            elif i=='-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            elif i=='/':
                stack.append(int(a/b))
        return stack.pop()
