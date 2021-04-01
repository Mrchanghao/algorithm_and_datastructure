'''
arr = [1, 1, 3, 2]

return 1

arr = [3, 4,2 ,3, 3]
return 3

제일 많이 있는 엘리먼트를 리턴 한다.

use map
'''

from collections import defaultdict


arr = list(map(int, input().split()))

'''
엘리먼트를 key로 하고 value를 하나씩 늘려 간 다음 value가 가장 많은 걸 리턴 
'''

def majorityElement(arr):
    m = {}
    for v in arr:
        m[v] = m.get(v, 0) + 1

    for v in arr:
        if m[v] >= (len(arr) // 2):
            return v


print(majorityElement(arr))




# print(m)




# print(dict)


