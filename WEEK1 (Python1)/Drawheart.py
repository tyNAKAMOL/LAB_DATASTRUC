n = int(input())
size = (n*4)-3

print(('.'*(n-1) + '*' + '.'*(n-2))*2+'.')
for i in range(2,n):
    left = ('.'*(n-i) + '*' + '+'* ((i-1)*2-1) + '*' + '.'*(n-i-1))
    print(left+'.'+left[1:]+'.')
print(('*' + '+'*((n*2)-3))*2+'*')
for i in range(1,(n*2)-2):
    print('.'*i + '*' + '+'* (size-(i+1)*2) + '*' + '.'*i)
print('.' * ((n*2)-2) + '*' + '.'*((n*2)-2))