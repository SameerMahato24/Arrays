def maximum_points(arr, k):
    left = 0
    right = len(arr) - 1
    ans = 0
    total = 0

    for i in range(k):
        total = total + arr[i]

    pointer = k - 1
    ans = max(total, ans)

    for _ in range(k):
        total = total - arr[pointer]
        total = total + arr[right]
        ans = max(total, ans)
        pointer = pointer - 1
        right = right - 1
    
    return ans

print(maximum_points([6,2,3,4,7,2,1,7,1], 4))