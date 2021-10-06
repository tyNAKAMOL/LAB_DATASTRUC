def numberBinary(n,digit):
    if n<=0:
        return str(int(bin(n)[2:])).zfill(digit)
    else:
        return numberBinary(n-1,digit) +"\n"+ str(int(bin(n)[2:])).zfill(digit)

n = int(input('Enter Number : '))
if n<0 :
    print("Only Positive & Zero Number ! ! !")
else:
    print(numberBinary((2**n)-1,n))
