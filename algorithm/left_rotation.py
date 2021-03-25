'''
5 3

[1, 2, 3, 4, 5]

5를 왼쪽으로 세번 이동한다

--> [2, 3, 4, 5, 1]
--> [3, 4, 5, 1, 2]
--> [4, 5, 1, 2, 3]  --> output

'''

def left_rotate(a, b):
    # rotate number b
    for j in range(b):
        first = a[0]
        # rotate 되면서 실행
        for i in range(len(a) - 1):
            a[i] = a[i + 1]
        a[len(a) - 1] = first

    return a

print(left_rotate([1, 2, 3, 4, 5], 3))