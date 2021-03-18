'''
M X N

row col

6 - 5, 7 4
1, 3, -6 10
8 -9 -3  7

가장 큰 사각형 의 합

'''
'''
max subarr sum
A 
A[0] A[1] A[2] ~ A[n]
maxIndex[0] ~ maxIndex[n]

'''

def max_subarr(arr):
    current_sum = 0
    max_sum = float('-inf')
    for i in range(len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(current_sum, max_sum)


    return max_sum


# 2d matrix sum

ROW = 4
COL = 5
M = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]

# Function call
# findMaxSum(M)
