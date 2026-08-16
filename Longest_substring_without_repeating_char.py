def lengthOfLongestSubstring(s):
    dic = {}
    longest = 0
    count = 0
    i = 0
    while(i < len(s)):
        if s[i] in dic:
            longest = max(count, longest)
            count = 0
            i = dic[s[i]] + 1
            dic = {}
            
        else:
            dic[s[i]] = i
            count += 1
            i += 1
    
    return max(count, longest)

print(lengthOfLongestSubstring("abcabcbb"))