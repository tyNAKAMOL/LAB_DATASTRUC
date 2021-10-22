class Queue:
    def __init__(self):
        self.List = []
    
    def enQ(self,x):
        self.List.append(x)
    
    def deQ(self):
        return self.List.pop(0)
    
    def rear(self):
        return self.List[-1]
    
    def isEmpty(self):
        return self.List == []
    
    def size(self):
        return len(self.List)

myQ = Queue()
yourQ = Queue()
myQ_= []
yourQ_ = []
score = 0
Act = {0 :'Eat',1:'Game',2:'Learn',3:'Movie'}
Location = {0 :'Res.',1:'ClassR.',2:'SuperM.',3:'Home'}  
inp = input("Enter Input : ").split(",")
for i in range(len(inp)):
    s = inp[i].split()
    myQ.enQ(s[0])
    myQ_.append(Act[int(myQ.rear()[0])] + ':' + Location[int(myQ.rear()[2])])
    yourQ.enQ(s[1])
    yourQ_.append(Act[int(yourQ.rear()[0])] + ':' + Location[int(yourQ.rear()[2])])
    if int(myQ.rear()[0]) == int(yourQ.rear()[0]) and int(myQ.rear()[2]) == int(yourQ.rear()[2]):
        score += 4
    elif int(myQ.rear()[0]) == int(yourQ.rear()[0]):
        score += 1
    elif  int(myQ.rear()[2]) == int(yourQ.rear()[2]):
        score += 2
    else: 
        score -= 5

print("My   Queue =",', '.join(myQ.List))
print("Your Queue =",', '.join(yourQ.List))
print("My   Activity:Location =",', '.join(myQ_))
print("Your Activity:Location =",', '.join(yourQ_))
if score >= 7 : print("Yes! You're my love! : Score is",str(score)+'.')
elif score <= 0 : print("No! We're just friends. : Score is",str(score)+'.')
else : print("Umm.. It's complicated relationship! : Score is",str(score)+'.')