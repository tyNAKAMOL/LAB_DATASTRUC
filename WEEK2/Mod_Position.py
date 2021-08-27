def mod_position(arr,s):
    x=[]
    if len(arr)==0 : return x
    else:
        if len(arr)%s==0 : x.append(arr[-1])
        return mod_position(arr[:-1],s) + x
        
print("*** Mod Position ***")
inp = input("Enter Input : ").split(',')
print(mod_position(inp[0],int(inp[1])))