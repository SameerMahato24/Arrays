def remove(arr):
    key = arr[0]
    index = 1
    count = 1
    for i in range(1, len(arr)):
        if(arr[i] > key):
            arr[index] = arr[i]
            index += 1
            count += 1
            key = arr[i]
    return arr, count

print(remove([1, 1, 1, 2, 3, 4, 4, 7, 8, 9, 9, 9, 10]))