def isSubsequence(s, t):
    left = 0
    right = 0
    isTrue = False

    if(s == ""):
        return True
    
    while(left < len(s) and right < len(t)):
        isTrue = False
        if(s[left] == t[right]):
            isTrue = True
            left += 1
        
        right += 1

    if(left != len(s)):
        return False

    return isTrue

print(isSubsequence("abc", "ahbgdc"))
    