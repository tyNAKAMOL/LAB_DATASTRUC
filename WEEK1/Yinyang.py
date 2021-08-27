n = int(input("Enter Input : "))

print('.'*((n+1))+'#'+'+'*(n+2))
for i in range(1,n+1):
    print('.'*((n+1)-i)+'#'*(i+1)+'+'+"#"*n+"+")
print('#'*(n+2)+'+'*(n+2))
print('#'*(n+2)+'+'*(n+2))
for i in range(1,n+1):
    print('#'+'+'*n+'#'+'+'*(n+2-i)+'.'*i)
print('#'*((n+2))+'+'+'.'*(n+1))