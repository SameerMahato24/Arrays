def searchRange(nums, target):
        x = lowerbound(nums, target)
        
        if x == -1 or nums[x] != target:
            return [-1, -1]
        
        y = upperbound(nums, target)
        
        return [x, y - 1]

def lowerbound(nums, target):
    low = 0
    high = len(nums) - 1
    lb = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return lb

def upperbound(nums, target):
    low = 0
    high = len(nums) - 1
    ub = len(nums)
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ub

print(searchRange([5, 7, 7, 8, 8, 10], 8))