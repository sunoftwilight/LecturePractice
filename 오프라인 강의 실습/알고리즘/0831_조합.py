# 조합 nCr
def comb(n, r):
    if r == 0:
        print(T)
        
    elif n < r:
        return 
    
    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


A = [1, 2, 3, 4]
N = len(A)
R = 3
T = [0] * R

comb(N, R)


# 중복 조합 nHr
def H(n, r):
    if r == 0:
        print(T)

    elif n == 0:
        return

    else:
        U[r-1] = A[n-1]
        H(n, r-1)
        H(n-1, r)


A = [1, 2, 3, 4]
N = len(A)
R = 3
U = [0] * R

H(N, R)


# 조합 계산 결과 출력하기
def com(n, r):
    if r == 0:
        return 1

    elif n < r:
        return 0

    else:
        return com(n-1, r-1) + com(n-1, r)


print(com(4, 3))
