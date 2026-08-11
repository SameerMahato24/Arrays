def union(arr1, arr2):
    result = []
    left = 0
    right = 0
    while(left < len(arr1) and right < len(arr2)):
        if arr1[left] == arr2[right]:
            if not result or result[-1] != arr1[left]:
                result.append(arr1[left])
            left += 1
            right += 1

        elif arr1[left] < arr2[right]:
            if not result or result[-1] != arr1[left]:
                result.append(arr1[left])
            left += 1

        else:
            if not result or result[-1] != arr2[right]:
                result.append(arr2[right])
            right += 1

    while left < len(arr1):
        if not result or result[-1] != arr1[left]:
            result.append(arr1[left])
        left += 1

    while right < len(arr2):
        if not result or result[-1] != arr2[right]:
            result.append(arr2[right])
        right += 1

    return result       

arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [1, 3, 4, 4, 5, 6, 7]      
print(union(arr1, arr2))