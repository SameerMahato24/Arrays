def arrayRankTransform(arr):
        arr1 = sorted(set(arr))

        rank = {}
        for i in range(len(arr1)):
            rank[arr1[i]] = i + 1

        result = []
        for num in arr:
            result.append(rank[num])

        return result
            

print(arrayRankTransform([40, 10, 20, 30]))