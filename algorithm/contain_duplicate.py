'''
return true if any value appear at least twice in the array
한 엘리먼트가 2번 이상 있으면 트루 리턴

아니면 false
'''
from collections import defaultdict

arr = list(map(int, input().split()))


def contain_duplicate(nums):
    # res = []
    settled = set(arr)
    return len(set(nums)) != len(nums)

def another_solution(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# print(another_solution(arr))



def third_solution(nums):
    m = defaultdict(int)
    for num in arr:
        if m[num]:
            return True
        m[num] += 1
        return False

print(third_solution([1, 2, 3, 3, 5]))

# def isPrime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         return True
#
