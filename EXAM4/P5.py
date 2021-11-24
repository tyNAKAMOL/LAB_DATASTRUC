comparison = 0
def mergeSort(ls):
    global comparison
    if len(ls) > 1:
        mid = len(ls)//2
        left = ls[:mid]
        right = ls[mid:]
        mergeSort(left)
        mergeSort(right)
        count1, count2, count3 = 0, 0, 0
        while count1 < len(left) and count2 < len(right):
            if left[count1] < right[count2]:
                ls[count3] = left[count1]
                count1 += 1
            else:
                ls[count3] = right[count2]
                count2 += 1
            count3 += 1
            comparison += 1
        while count1 < len(left):
            ls[count3] = left[count1]
            count1 += 1
            count3 += 1
        while count2 < len(right):
            ls[count3] = right[count2]
            count2 += 1
            count3 += 1

def printAns(inp):
    for i in range(len(inp)):
        print(inp[i], end=" ")

print(' *** Merge sort ***')
inp = [int(i) for i in input('Enter some numbers : ').split(' ')]
mergeSort(inp)
print("\nSorted -> ", end='')
printAns(inp)
print('\nData comparison = ', comparison)