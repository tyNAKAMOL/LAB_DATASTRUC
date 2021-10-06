class Queue:
    def __init__(self):
        self.List = []
    
    def enQ(self,x):
        self.List.append(x)
    
    def deQ(self):
        return self.List.pop(0)
    
    def isEmpty(self):
        return self.List == []
    
    def size(self):
        return len(self.List)

Q = Queue()
inp = input("Enter Input : ").split(",")
for i in range(len(inp)):
    s = inp[i].split()
    if s[0]=='E':
        Q.enQ(s[1])
        print(Q.size())
    else:
        if not Q.isEmpty() : print(Q.deQ(),'0')
        else : print('-1')
if not Q.isEmpty():
    print(' '.join(Q.List))
else:
    print('Empty')

