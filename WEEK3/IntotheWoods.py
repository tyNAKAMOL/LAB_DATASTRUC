class Stack:
    def __init__(self, data=None):
        if data is not None:
            self.items = data
        else:
            self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
inp = input('Enter Input : ').split(',')
for i in range(len(inp)):
    x = inp[i].split()     
    if x[0]=='A':
        if stack.isEmpty():
            stack.push(int(x[1]))
        else:
            while not stack.isEmpty() and int(x[1]) >= stack.peek():
                stack.pop()
            stack.push(int(x[1]))
    else:print(stack.size())