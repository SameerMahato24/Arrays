def move(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1

    return arr

arr = [0, 1, 0, 3, 12]
print(move(arr))

# l = len(arr)
#     start = 0
#     end = 0
#     for i in range(l):
#         if(arr[i] == 0):
#             end = i
#             break

#     start = end + 1
#     while(start < l):
#         if(arr[start] != 0):
#             arr[start], arr[end] = arr[end], arr[start]
#             end += 1

#         start += 1

#     return arr
    

# arr = [1,0, 2, 3, 2, 0, 0, 4, 5, 1]
# print(move(arr))    