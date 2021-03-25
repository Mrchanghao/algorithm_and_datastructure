'''
[1, 1, 2]

이미 sorting 되어 있는 arr 에서 연속으로 나와 있는 element를 삭제한 arr의 길이
--> return 2 --> because [1, 2]
'''


def remove_duplicate(arr):
    if len(arr) == 0: return 0

    i = 0  # first pointer
    for j in range(len(arr)):
        #     second pointer 지정
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1


print(remove_duplicate([1, 1, 1, 2]))
