arr = list(map(int, input().split()))
n = len(arr)

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = a[j+1], arr[j]

print(arr)
