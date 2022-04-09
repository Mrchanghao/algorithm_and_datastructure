# util function 

def swap_two(arr, a_index, b_index):
    result = [arr[a_index], arr[b_index]] = [arr[b_index], arr[a_index]]
    return result


def sort_two(arr, a_index, b_index):
    if(arr[a_index] > arr[b_index]):
        swap_two(arr, a_index, b_index)
        
        
def bubble_sort(arr):
    index = len(arr) - 1
    sort = False 
    while not sort:
        sort = True 
        for i in range(index):
            if arr[i] > arr[i + 1]:
                sort = False 
                swap_two(arr, i, i + 1)
    return arr 


def selection_sort(arr):
    min = 0
    for i in range(0, len(arr)):
        min = i 
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[min]):
                min = j
        if min != i:
            swap_two(arr, min, i)
    return arr 

def merge(arr1, arr2):
    merged = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr 
    low, high = 0, len(arr) - 1
    mid = (low + high) // 2
    left = (arr[0:mid])
    right = (arr[mid:])
    return merge(left, right)

            

arr = [11, 45, 53, 1, 2, 10]
merge_sort(arr)
print(merge_sort(arr))