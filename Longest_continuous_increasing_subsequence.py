def findLengthOfLCIS(nums):
    count = 1
    total = 0
    i = 0
    while(i < len(nums)-1):
        if(nums[i] < nums[i + 1]):
            count += 1
            i += 1

        else:
            total = max(count, total)
            count = 1
            i += 1

    return max(count, total)

print(findLengthOfLCIS([1,3,5,4,7]))