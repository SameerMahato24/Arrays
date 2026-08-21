def maxRotateFunction(nums):
        n = len(nums)

        total = sum(nums)

        # Calculate F(0)
        f = 0
        for i in range(n):
            f += i * nums[i]

        ans = f

        # Calculate F(1) to F(n-1)
        for i in range(n - 1, 0, -1):
            f = f + total - n * nums[i]
            ans = max(ans, f)

        return ans

print(maxRotateFunction([4, 3, 2, 6]))  # Output: 26

        