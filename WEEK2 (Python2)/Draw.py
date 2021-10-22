def abs(x):
    return (x*(-1)) if x<0 else x

def draw(L,R):
    if R==0:
        return ''
    if L<0:
        return draw(L,R+1) + "_"*(abs(R+1))+'#'*(abs(L)-abs(R)+1)+'\n' 
    return draw(L,R-1) + "_"*(L-R)+'#'*(R)+'\n'

n = int(input("Enter Input : "))
print(draw(n,n),end='')
