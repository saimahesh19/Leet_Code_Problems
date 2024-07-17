class MyQueue:
    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        if self.empty():
            return None
        temp_stack = []
        while len(self.stack) > 1:
            temp_stack.append(self.stack.pop())
        front = self.stack.pop()
        while temp_stack:
            self.stack.append(temp_stack.pop())
        return front
        
    def peek(self) -> int:
        if self.empty():
            return None
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
