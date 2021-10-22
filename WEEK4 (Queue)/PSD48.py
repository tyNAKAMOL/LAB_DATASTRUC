class Queue:
    def __init__(self):
        self.List = []
    
    def enQ(self,x):
        self.List.append(x)
    
    def deQ(self):
        return self.List.pop(0)
    
    def add_first(self,index,x):
        self.List.insert(index,x)
    
    def rear(self):
        return self.List[-1]
    
    def front(self):
        return self.List[0]
    
    def isEmpty(self):
        return self.List == []
    
    def size(self):
        return len(self.List)

Q = Queue()
es = []
inp = input("Enter Input : ").split(",")
for i in range(len(inp)):
    s = inp[i].split()
    if s[0] == 'EN':
        Q.enQ(s[1])
    elif s[0] == 'ES':
        Q.add_first(len(es),s[1])
        es.append(s[1])
    elif s[0] == 'D':
        if not Q.isEmpty() :
            print(Q.front())
            if len(es):
                if Q.front() == es[0]:
                    es.pop(0)
            Q.deQ()
        else:
            print('Empty')
