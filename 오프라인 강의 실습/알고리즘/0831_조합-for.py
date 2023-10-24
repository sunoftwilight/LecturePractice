# 조합으로 선택한 요소 출력하기

a = [1, 2, 3, 4]
N = len(a)

for i in range(N-2):
    for j in range(i+1, N):
        print(a[i], a[j])
print("==================================")
'''
1 2
1 3
1 4
2 3
2 4
'''

a = [1, 2, 3, 4]
N = len(a)

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(a[i], a[j], a[k])
print("==================================")
'''
1 2 3
1 2 4
1 3 4
2 3 4
'''


def comb(n, r, k, s):            # s는 시작 숫자
    if r == k:
        print(T)

    else:
        for i in range(s, n-r+1+k):           # n-r+1 : 선택 가능한 마지막 원소
            T[k] = a[i]
            comb(n, r, k+1, i+1)


a = [1, 2, 3, 4]
N = len(a)
R = 3
T = [0] * R

comb(4, 3, 0, 0)

'''
[1, 2, 3]
[1, 2, 4]
[1, 3, 4]
[2, 3, 4]
'''