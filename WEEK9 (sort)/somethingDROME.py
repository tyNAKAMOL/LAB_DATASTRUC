def drome(inp):
    x=0
    y=0
    z=0
    duplicate = False
    for i in range(len(inp)-1):
        if inp[i]>inp[i+1]:
            x += 1
        elif inp[i]<inp[i+1]:
            y += 1
        elif inp[i]==inp[i+1]:
            duplicate = True
            z+=1
            
    if z==len(inp)-1:print("Repdrome")
    elif duplicate and y+z==len(inp)-1:print("Plaindrome")
    elif not duplicate and y+z==len(inp)-1:print("Metadrome")
    elif duplicate and x+z==len(inp)-1:print("Nialpdrome")
    elif not duplicate and x+z==len(inp)-1:print("Katadrome")
    else : print("Nondrome")


inp = [int(i) for i in input("Enter Input : ")]
drome(inp)

