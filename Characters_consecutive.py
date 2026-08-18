def maxPower(s):
    count = 0
    total = 0
    right = 0
    last_elem = s[0]
    while(right < len(s)):
        if(s[right] == last_elem):
            count += 1
            
        else:
            total = max(count, total)
            last_elem = s[right]
            count = 1
            
        right += 1
    return max(count, total)

print(maxPower("leetcode"))