'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

element를 한번 for 돌린 다음 그 엘리먼트를 다시 for로 돌린다
그 엘리먼트들이

hashmap으로 풀이 한다

for str in input
    hash = findhash(str)  str --> str을 sorting한
    hashMap[hash].append(str)

for value in hashmap.value:
    answer.append(value)
'''


def findHash(str):
    return ' '.join(sorted(str))


def group_anagram(str_arr):
    result = []
    m = {}

    for s in str_arr:
        # sorting version
        hashed = findHash(s)
        if hashed not in m:
            m[hashed] = []
        m[hashed].append(s)

    for p in m.values():
        result.append(p)

    return result


# group_anagram(["eat", "tea", "tan"])
print(group_anagram(["eat", "tea", "tan"]))
