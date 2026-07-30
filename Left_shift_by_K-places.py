def rotatearray(arr, k):
    l = len(arr)
    rotate = k % l  # Handle cases where k is greater than the length of the array
    temp = []
    for i in range(rotate):
        temp.append(arr[i])

    for i in range(rotate, l):
        arr[i - rotate] = arr[i]

    for j in range(l - rotate, l):
        arr[j] = temp[j - (l - rotate)]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotatearray(arr, k))
