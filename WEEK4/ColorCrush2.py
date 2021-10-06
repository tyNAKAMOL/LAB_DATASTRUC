class ColorCrush:
    def __init__(self,item=None):
        if item is not None:
            self.item = item
        else:
            self.item = []
    
    def push(self,data):
        self.item.append(data)
    
    def pop(self):
        return self.item.pop(0)

    def rear(self):
        return self.item[-1]
    
    def front(self):
        return self.item[0]
    
    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []

def same(x,y,z):
    return x == y == z

Normal , Mirror = input("Enter Input (Normal, Mirror) : ").split()
Normal , Mirror = list(Normal) , list(Mirror[::-1])
temp = []
NorEx,MirEx,fail,bom = 0,0,0,0
Boom = ColorCrush()
i=0
while i in range(len(Mirror)-2):
    if same(Mirror[i],Mirror[i+1],Mirror[i+2]):
        Boom.push(Mirror[i]) 
        MirEx += 1
        for j in range(3):
            Mirror.pop(i)
        i=-1
    i+=1
i=0                                                                   
while i in range(len(Normal)-2):
    bom = -1
    if same(Normal[i],Normal[i+1],Normal[i+2]):
        if not Boom.isEmpty():
            for j in range(len(Normal)-(i+2)):
                temp.append(Normal.pop())
            Normal.append(Boom.pop())
            for k in range(len(temp)):
                Normal.append(temp.pop())
            bom = i
    if same(Normal[i],Normal[i+1],Normal[i+2]):
        for j in range(3):
            Normal.pop(i)
        if i == bom:
            fail+=1
        else:
            NorEx+=1        
        i=-1
    i+=1

print("NORMAL :")
print(len(Normal))
print(''.join(Normal[::-1])if len(Normal) else "Empty")
print(NorEx,"Explosive(s) ! ! ! (NORMAL)")
if fail:
    print("Failed Interrupted",fail,"Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(len(Mirror))
print(''.join(Mirror[::-1]) if len(Mirror) else "ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE",MirEx)

