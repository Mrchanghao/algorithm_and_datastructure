def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        
        if arr[mid] < target:
            low = mid + 1
        
        if arr[mid] == target:
            return mid
    return -1


def binary_search_recursion(arr, target):
    low, high = 0, len(arr) - 1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        binary_search_recursion(arr)

print(binary_search([1, 3, 4, 5, 6, 7, 8, 9], 4))

'''
element가 많아질 수록 효율이 커진다
'''