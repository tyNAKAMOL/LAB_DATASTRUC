def FirstGreaterValue(list_,value):
    if value>list_[-1]:
        print("No First Greater Value")
    else:
        for i in range(len(list_)):
            if list_[i] > value:
                print(list_[i])
                break
                
    
x,y = input("Enter Input : ").split("/")
x = sorted([int(i) for i in x.split()])
y = [int(i) for i in y.split()]
for i in y:
    FirstGreaterValue(x,i)

