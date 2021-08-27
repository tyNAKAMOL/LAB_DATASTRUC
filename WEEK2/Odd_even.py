ls = []
def odd_even(arr,s,i):
    if len(arr)>0:
        if (i%2==0 if s[0]=='O' else i%2==1):
            ls.append(arr[0])
        return odd_even(arr[1:],s[0],i+1)

print("*** Odd Even ***")
inp = input("Enter Input : ").split(',')
if inp[0]=='L':
    odd_even(inp[1].split(),inp[2],0)
    print(ls)
else:
    odd_even(inp[1],inp[2],0)
    print(''.join(ls))


