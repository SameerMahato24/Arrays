def mirrorDistance(n):
        digit = 0
        ans = n
        while(n > 0):
            r = n % 10
            digit = digit * 10 + r
            n = n // 10
        return abs(ans - digit)

print(mirrorDistance(123))  # Output: 198