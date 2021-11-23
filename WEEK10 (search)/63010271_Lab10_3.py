class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def Newindex(self,lst,value,n, maxCol):
        j = 0
        k = value
        print("collision number {} at {}".format(j+1, k))
        while j < maxCol-1:
            j += 1
            k = (value + (j*j)) % n
            if lst[k] == None:
                return k
            else:
                print("collision number {} at {}".format(j+1, k))
        return -1

num, inp = input(" ***** Fun with hashing *****\nEnter Input : ").split('/')
num = num.split()
inp = inp.split(',')
table = int(num[0])
maxCollision = int(num[1])
lst_ = [None]*table
size = 0
h = hash()
for i in inp:
    if size != table:
        key,val = i.split()
        s = sum(ord(i) for i in key)
        n = s % table
        # print(s,n)

        if lst_[n] == None:
            lst_[n] = Data(key, val)
            size += 1
        else: #collision
            index = h.Newindex(lst_,n,table,maxCollision) 
            if index != -1:
                lst_[index] = Data(key, val)
                size += 1
            else:
                print("Max of collisionChain")
        
        for k in range(0, len(lst_)):
            print("#"+str(k+1), end="      ")
            print(lst_[k])
        print("---------------------------")
    else:
        print("This table is full !!!!!!")
        break



