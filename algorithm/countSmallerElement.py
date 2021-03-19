'''
count smaller element present in the arr for each arr element
[3, 4, 1, 1, 2]
[3, 4, 0, 0, 2]

'''
# approach 1 array traverse
arr = list(map(int, input().split()))



for i in range(len(arr)):
    count = 0
    for j in range(0, len(arr)):
        if arr[j] < arr[i]:
            count += 1
        # print(arr[j], arr[i])
    print(count, end=' ')

# 3 4 0 0 2  --> printed

# approach 2 using hashing
