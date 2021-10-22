class Torkham:

    def __init__(self, words = None):
        self.check = True
        if words is not None:
            self.words = words
        else:
            self.words = []
    
    def restart(self):
        self.words = []
        return "game restarted"

    def match(self,lst1,lst2):
        return lst1[-2:].upper()==(lst2)[:2].upper()
    
    def gameOver(self):
        return "game over"
    
    def isEmpty(self):
        return self.words == []
    
    def checkInput(self,key):
        if key!='P' and key!='R' and key!='X': self.check = False
        return self.check

    def inputInvalid(self):
        return "is Invalid Input !!!"  
        
    def peek(self):
        return self.words[-1]

    def push(self, arr):
        self.words.append(arr)
    
    def getList(self):
        return self.words


T = Torkham()
print("*** TorKham HanSaa ***")
inp = input("Enter Input : ").split(',')
for i in range(len(inp)):
    s = inp[i].split()
    if T.checkInput(s[0]):
        if s[0]=='P':
            if T.isEmpty():
                T.push(s[1])
            elif T.match(T.peek(),s[1]):
                T.push(s[1])
            else:
                print("'{}' -> ".format(s[1])+T.gameOver())
                break
            print("'{}' ->".format(s[1]),T.getList())
        elif s[0]=='R':
            print(T.restart())
        elif s[0]=='X':
            break
    else:
        if s[0]!='r'and s[0]!='x':
            print("'{}' -> ".format(inp[i])+T.inputInvalid())
        else:
            print("'{}' -> ".format(s[0])+T.inputInvalid())
        break
            





























