def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0 :
            if i<0 or nums1[i] <= nums2[j]:
                    nums1[k] = nums2[j]
                    k = k - 1
                    j = j - 1
            else:
                    nums1[k] = nums1[i]
                    k = k-1
                    i = i-1
    return nums1 
                       
nums1 = [-1,0,0,1,2,3,0,0,0]
nums2 = [1,2,3]
m = 6
n = 3
print(merge(nums1, m, nums2, n))
