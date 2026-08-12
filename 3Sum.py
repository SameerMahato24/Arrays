def threesum(arr):
    result = set()
    for i in range(len(arr)):
        my_set = set()
        for j in range(i+1, len(arr)):
            complement = -arr[i] - arr[j]
            if complement in my_set:
                result.add(tuple(sorted((arr[i], arr[j], complement))))
            my_set.add(arr[j])
    return [list(triplet) for triplet in result]

print(threesum([-1, 0, 1, 2, -1, -4]))