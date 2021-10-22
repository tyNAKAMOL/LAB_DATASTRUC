class funString():

    def __init__(self,s):
        self.arr = s

    def __str__(self):
        return "Hello"


    def size(self) :
        return len(self.arr)

    def changeSize(self):
        x=[]
        for i in self.arr:
            if 65<=ord(i)<=90:
                x.append(chr(ord(i)+32))
            else:
               x.append(chr(ord(i)-32))
        return ''.join(x)


    def reverse(self):
        return self.arr[::-1]

    def deleteSame(self):
        x=[]
        for i in range(len(self.arr)):
            if self.arr[i] not in x:
                x.append(self.arr[i])
        return ''.join(x)





str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())