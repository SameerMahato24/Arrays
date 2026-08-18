def appendCharacters(s, t):
        count = 0
        left = 0 
        right = 0
        
        while(left < len(s) and right < len(t)):
            if(s[left] == t[right]):
                count += 1
                right += 1
            
            left += 1

        return len(t) - count

print(appendCharacters("coaching", "coding"))