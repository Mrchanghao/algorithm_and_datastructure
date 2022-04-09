"""
two sum
arr, target_sum
"""


def two_sum(arr, target_sum):
    res = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            if arr[j] + arr[i] == target_sum:
                return [i, j]

# # 타겟에서 뺀 수를  결과를 키로 조회

def two_sum_with_hash(nums, target):
    hash = {}
    for i, val in enumerate(nums):
    
        hash[val] = i
    
    for j, val in enumerate(nums):
        if (target - val) in hash and j != hash[target - val]:
            return [j, hash[target - val]]


print(two_sum([1, 2, 3, 9, 12], 5))
print(two_sum_with_hash([1, 2, 3, 9, 12], 5))
