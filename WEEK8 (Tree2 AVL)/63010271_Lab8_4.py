def Mondstadt(n):
    sum = 0                            
    if n >= len(power):             
        return 0
    sum += Mondstadt(2*n + 1)     
    sum += Mondstadt(2*n + 2)     
    return power[n] + sum           

power, group = input('Enter Input : ').split('/')
power = [int(i) for i in power.split()]
group = [str(i) for i in group.split(',')]
print(Mondstadt(0))                 
for x in range(len(group)):
    i,j = group[x].split()
    n1 = Mondstadt(int(i))        
    n2 = Mondstadt(int(j))          
    if n1 > n2 : print("{}>{}".format(i,j))
    elif n1 < n2 : print("{}<{}".format(i,j))
    else : print("{}={}".format(i,j))