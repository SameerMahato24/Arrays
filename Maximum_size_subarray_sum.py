def maximum_subarray(nums, target):
    low = 0
    high = 0
    add = 0
    length = 0
    while(high < len(nums)):
        
        add += nums[high]
        
        while(add > target):
            add = add - nums[low]
            low += 1
            
        length = max(length, high - low + 1)
        high += 1

    return length

print(maximum_subarray([2,5,1,7,1,4], 14))