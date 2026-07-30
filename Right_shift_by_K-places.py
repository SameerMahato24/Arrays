def rotate(arr, k):
    l = len(arr)
    rotate = k % l
    temp = []
    for i in range(0, l-rotate):
        temp.append(arr[i])

    for i in range(l-rotate, l):
        arr[i-(l-rotate)] = arr[i]

    for j in range(rotate,l):
        arr[j] = temp[j - rotate]
        
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(arr, k))
