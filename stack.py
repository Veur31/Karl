class Stack:
    def __init__(self):
        self.stack= []

    def push(self, num):
        self.stack.append(num)
        print(self.stack)
    def pop(self):
        self.stack.pop()
        print(self.stack)
    def peek(self):
        peek = self.stack[-1]
        print(peek)

stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
stack.peek()

        