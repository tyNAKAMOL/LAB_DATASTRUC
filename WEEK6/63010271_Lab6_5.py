def abs(n):
    if n<0 : return n*(-1)
    else : return n

def asteroid_collision(asts,lst):
    if lst == []:
        return asts
    else:
        if asts == []:
            return asteroid_collision(asts+[lst[0]],lst[1:])
        elif (asts[-1] < 0 and lst[0] < 0) or (asts[-1] > 0 and lst[0] > 0):
            return asteroid_collision(asts+[lst[0]],lst[1:])
        elif asts[-1] < 0 and lst[0] > 0 :
            return asteroid_collision(asts+[lst[0]],lst[1:])
        else:
            if abs(asts[-1]) > abs(lst[0]):
                return asteroid_collision(asts,lst[1:])
            elif abs(asts[-1]) == abs(lst[0]):
                return asteroid_collision(asts[:-1],lst[1:])
            else:
                return asteroid_collision(asts[:-1],lst)

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision([],x))