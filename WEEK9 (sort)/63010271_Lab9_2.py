def sort_list(arr,n,m):
    if n == len(arr)-1:
        n = 0
        m += 1 
    if m == len(arr): return
    if arr[n]>=0 and arr[m]>=0:
        if arr[n] > arr[m]:
            arr[n],arr[m] = arr[m],arr[n]
    sort_list(arr,n+1,m)
    return arr

inp = [int(i) for i in input('Enter Input : ').split()]
print(*sort_list(inp,0,0))