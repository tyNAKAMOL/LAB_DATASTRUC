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

def calculate(op,x,y):
    if op == "*": 
        return x * y 
    elif op == "/":
        return x / y 
    elif op == "+": 
        return x + y 
    elif op == "-": 
        return x - y 
    else:
        return x**y

def postFixeval(st):
    stack = Stack()
    Operators = ["+", "-", "*", "/", "(", ")", "^"]
    for i in st:
        if i not in Operators:
            stack.push(int(i))
        else:
            top = stack.pop()
            Ltop = stack.pop()
            stack.push(calculate(i,Ltop,top))
    return stack.pop()

print(" ***Postfix expression calcuation***")
n = input("Enter Postfix expression : ").split()
print("Answer : ",'{:.2f}'.format(postFixeval(n)))
