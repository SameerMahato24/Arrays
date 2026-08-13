def rearrange(arr):
    l = len(arr)
    result = [0] * l
    left = 0
    right = 1
    for i in  range(l):
        if(arr[i] >= 0):
            result[left] = arr[i]
            left += 2
        else:
            result[right] = arr[i]
            right += 2
    return result

print(rearrange([5,10,-3,-1,-10,6]))