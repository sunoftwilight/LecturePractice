# nㅠr (중복 순열)
def perm(n, k, r):    # 원소 개수 n, depth k
    if r == k:
        print(p)
        return

    else:
        for i in range(n):
            # if visited[i] == 0:
            #     visited[i] = 1
                p[k] = a[i]
                perm(n, k+1, r)
                # visited[i] = 0


a = [1, 2, 3]
N = len(a)
R = 2
p = [0] * R
# visited = [0] * N

perm(N, 0, R)
