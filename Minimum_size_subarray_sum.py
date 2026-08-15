def minSubArrayLen(target, nums):
    low = 0
    high = 0
    add = 0
    length = float("inf")
    for high in range(len(nums)):
        
        add += nums[high]
        
        while add >= target:
            length = min(length, high - low + 1)
            add -= nums[low]
            low += 1

    return 0 if length == float('inf') else length

print(minSubArrayLen(7, [2,3,1,2,4,3]))