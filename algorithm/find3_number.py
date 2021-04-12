'''

target sum 이 나오는

3 element 를 구해라
'''

def find3Numbers(A, arr_size, sum):
    # sorting 먼저
    A.sort()
    # 첫번째 엘리먼트를 고정하고
    # 하나씩 바꿔 가며 다른 두개의 엘리먼트를 찾는다
    result = []
    for i in range(0, arr_size -2):
        # start two index variables from two corners of the arr and move them
        # toward each other
        # index of the first element
        # in the remain elements
        l = i + 1

        r = arr_size - 1
        while l < r:
            if (A[i] + A[l] + A[r] == sum):

                return [A[i], A[l], A[r]]

            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            elif (A[i] + A[l] + A[r] > sum):
                r -= 1

    return []


A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)

print(find3Numbers(A, arr_size, sum))


def find3NumbersWithHashing(A, arr_size, sum):
    for i in range(0, arr_size - 1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to sum - A[i]
        s = set()
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if (curr_sum - A[j]) in s:
                print("Triplet is", A[i],
                      ", ", A[j], ", ", curr_sum - A[j])
                return True
            s.add(A[j])

    return False
