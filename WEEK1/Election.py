print("*** Election ***")
n = int(input("Enter a number of voter(s) : "))
num = list(map(int,(input().split())))
arr = [0]*21
for i in num:
    if i >= 1 and i <=20 :
        arr[i] = arr[i] + 1

if sum(arr) == 0:
    print("*** No Candidate Wins ***")
else:
    MAX = max(arr)
    for i in range(0,20):
        if arr[i] == MAX:
            print(i)
            break