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
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

print(" *** Stack implement by Python list***")
inp = input("Enter data to stack : ").split()
stack = Stack()
for i in inp:
    stack.push(i)
print(stack.size(),"Data in stack : ",stack.items)
while not stack.isEmpty():
    stack.pop()
print(stack.size(),"Data in stack : ",stack.items)