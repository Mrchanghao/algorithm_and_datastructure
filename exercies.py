def sort012(arr, arr_size):
    arr_size = len(arr)
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo = lo + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi = hi - 1
    return arr

def printArr(arr):
    for k in arr:
        print(k, end=" ")


# testArr = [1, 0, 1, 1, 0, 1, 1 ,2 ,2, 0, 0, 1, 0, 1, 2]
# adjustArr = sort012(testArr, len(testArr))
#
# printArr(adjustArr)


'''
given value N --> make change for N cents 
ex) N = 4 ==> S = { 2, 2},  {1, 1, 1, 1} {1, 1, 2} {1, 3}  --> output return 4 

ex) N = 10 --> S = 
'''
def coinChange(S, m, n):
    if (n == 0):
        return 1

    if (n < 0):
        return 0

    if (m <= 0 and n >= 1):
        return 0

    return coinChange(S, m - 1, n) + coinChange(S, m, n-S[m-1])

