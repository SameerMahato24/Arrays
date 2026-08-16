def maximum_points(arr, k):
    left = 0
    right = len(arr) - 1
    ans = 0
    total = 0
    while(left <= k):
        for i in range(k-left):
            total += arr[i]

        for _ in range(left):
            total = total + arr[right]
            right -= 1

        right = len(arr) - 1
        ans = max(ans, total)
        total = 0
        left += 1

    return ans

print(maximum_points([6,2,3,4,7,2,1,7,1], 4))