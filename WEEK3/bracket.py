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
inp = input("Enter expresion : ")
bk = {'(':')','{':'}','[':']'}
Unmatched = False
for i in inp:
    if i in bk.keys() or i in bk.values():
        if i in bk.keys() or stack.isEmpty():
            stack.push(i)
            if i in bk.values():
                stack.pop()
                print(inp,"close paren excess")
                Unmatched = True
                break
        else:
            if bk[stack.peek()] != i:
                print(inp,"Unmatch open-close")
                Unmatched = True
                break
            else:
                stack.pop()
    else:continue

if Unmatched==False:
    if stack.isEmpty() : print(inp,"MATCH")
    else : print(inp,"open paren excess  ",stack.size(),':',''.join(stack.items))



