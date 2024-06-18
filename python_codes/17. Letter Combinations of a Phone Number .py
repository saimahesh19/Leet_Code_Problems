class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        
        queue = deque([''])
        
        for digit in digits:
           
            n = len(queue)
            for _ in range(n):
                
                combination = queue.popleft()
                
                for letter in digit_to_letters[digit]:
                    queue.append(combination + letter)
        
        return list(queue)


