def ncr(n, r, s):             # n개 중 r개를 고르는 조합, 선택할 수 있는 구간의 시작 s
    if r == 0:
        print(*comb)

    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            ncr(n, r-1, i+1)


A = [1, 2, 3, 4, 5]
N = len(A)
R = 3
comb = [0] * R

ncr(N, R, 0)
