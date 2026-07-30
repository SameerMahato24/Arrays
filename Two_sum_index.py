def twoSum(nums, target):
    l=[]
    for i in nums:
        p=nums.index(i)
        for j in range(p+1,len(nums)):
            if((i+nums[j])==target):
                l.append(nums.index(i))
                l.append(j)

    print(l[:2])

nums=[2,5,5,11]
target=10
twoSum(nums,target)
                
