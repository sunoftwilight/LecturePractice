# nPn
def perm(n, k):    # 원소 개수 n, depth k
    if n == k:
        print(p)
        return

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = a[i]
                perm(n, k+1)
                visited[i] = 0


a = [1, 2, 3]
N = len(a)
p = [0] * N
visited = [0] * N

perm(N, 0)

'''
집(1)에서 출발해서 2, 3, 4 들렀다가 집(1)으로 다시 돌아오는 법?
=> 1은 고정해두고 2, 3, 4로만 순열 돌려야됨

a = [1, 2, 3, 4]
N = len(a)

p = [0] * (N + 1)    # 하나 크게 p 잡아두기
p[0] = p[N] = a[0]

visited = [0] * N
visited[0] = 1       # 고정시켜두기

perm(N, 1)           # 1부터 시작
'''