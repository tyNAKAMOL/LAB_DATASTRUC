print("*** Fun with Drawing ***")
k = int(input("Enter input : "))
size = 4*k-3
x = [['#' for i in range(size)] for j in range(size)]
for i in range(size):
    if i % 2:
        for j in range(i, size-i):
            x[i][j] = '.'
            x[size-i-1][j] = '.'
        for j in range(i, size-i):
            x[j][i] = '.'
            x[j][size-i-1] = '.'
for i in range(size):
    for j in range(size):
        print(x[i][j], end='')
    print()