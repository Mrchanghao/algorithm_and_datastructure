'''
bubble sort

'''


def bubble_sort(list):
    index = len(list) - 1
    sort = False

    while not sort:
        sort = True
        for i in range(index):
            if list[i] > list[i + 1]:
                sort = False
                list[i], list[i + 1] = list[i + 1], list[i]
    # index = index - 1


arr = [45, 53, 1, 32, 11, 22, 8, 7]
bubble_sort(arr)
print(arr)
