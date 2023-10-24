N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = []
dj = []

max_v = 0

for i in range(N):
    for j in range(M):
        s = arr[i][j]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N:   # 배열을 벗어나지 않으면
                s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합

        if max_v < s:
            max_v = s
