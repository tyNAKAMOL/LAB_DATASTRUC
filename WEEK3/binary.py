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

def dec2bin(n):
    stack = Stack()
    while n!=1:
        stack.push(n%2)
        n=int(n/2)
    stack.push(n)
    return ''.join(list(map(str,stack.items[::-1])))

print(" ***Decimal to Binary use Stack***")
m = input("Enter decimal number : ")
if int(m)==0 : print("Binary number : 0")
else:
    print("Binary number : ",end='')
    print(dec2bin(int(m)))