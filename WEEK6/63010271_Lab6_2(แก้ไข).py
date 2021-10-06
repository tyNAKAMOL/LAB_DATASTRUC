def length(txt):
    n = 0
    if txt == '':return 0
    n += length(txt[:-1]) + 1
    if n%2 : print(txt[-1] + "*",end='')
    else : print(txt[-1] + "~",end='')
    return n

inp = input("Enter Input : ")
print('\n' + str(length(inp)))

