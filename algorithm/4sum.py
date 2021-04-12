'''

return the number of tuples (i, j, k, l) such that:
nums1[i] + nums2[j] + nums3[k] + nums[l] == 0
1 -2   -1    -1   0   -1
2  -1  1      2   2   4
1 -1  0       -1  2   1
2 -2  0       2   0   2
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
'''


def fourSumCount(num1, num2, num3, num4):
    m = {}
    a = len(num1)
    b = len(num2)
    c = len(num3)
    d = len(num4)
    result = 0
    for i in range(0, a):
        x = num1[i]
        for j in range(0, b):
            y = num2[j]

            if x + y not in m:
                m[x + y] = 0

            m[x + y] += 1

    for i in range(0, c):
        x = num3[i]
        for j in range(0, d):
            y = num4[j]
            target = -(x + y)
            if target in m:
                result += m[target]

    return result

# 다시 풀어 본다
