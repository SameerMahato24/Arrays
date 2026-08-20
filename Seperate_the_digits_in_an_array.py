def separateDigits(nums):
        answer = []
        for i in nums:
            for j in str(i):
                answer.append(int(j))
        return answer

print(separateDigits([13, 25, 83, 77]))