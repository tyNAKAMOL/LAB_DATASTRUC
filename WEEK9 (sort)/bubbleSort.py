def bubble_sort(arr,n,m):
    if n == len(arr)-1:
        n = 0
        m += 1 
    if m == len(arr): return
    if arr[n] > arr[m]:
        arr[n],arr[m] = arr[m],arr[n]
    bubble_sort(arr,n+1,m)
    return arr

inp = [int(i) for i in input("Enter Input : ").split()]
print(bubble_sort(inp,0,0))