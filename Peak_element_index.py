'''def peak(lst):
    start=0
    end=len(lst)-1
    while(start!=end):
        if(lst[start]>lst[end]):
            end-=1
        elif(lst[start]<lst[end]):
            start+=1
        elif(lst[start]==lst[end]):
            start+=1
            end-=1
    return start
lst=[2,3,4,5,6,6,7,5,4,3,2,1]
print(peak(lst))'''
# 90 degree rotation matrix
# matrix=[]
# m=4
# n=4
# for i in range(m):
#     data=[]
#     for j in range(n):
#         x=int(input())
#         data.append(x)
#     matrix.append(data)

# print("Your matrix")
# print(matrix)

# arr = []
# for i in range(m-1,-1,-1):
#     arr1 = []
#     for j in range(n):
#         arr1.append(matrix[j][i])
#     arr.append(arr1)
    
# print(arr)
# result = []
# for i in arr:
#     result.append(i[::-1])
# print(result[::-1])

def transpose(matrix):
    arr = []
    for i in range(len(matrix)):
        data=[]
        for j in range(len(matrix[i])):
            data.append(matrix[j][i])
        arr.append(data)
    print(arr)


matrix = [[1,2,3],[4,5,6]]
transpose(matrix)