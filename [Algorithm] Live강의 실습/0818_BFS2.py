'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, V):   # 시작 정점 s, 마지막 정점 v
    visited = [0] * (V + 1)        # visited 생성
    q = []                         # 큐 생성
    q.append(s)                    # 시작점 인큐
    visited[s] = 1                 # 시작점 방문 표시

    while q:                       # q에 정점이 남아있으면 (front, rear 썼다면 front != rear)
        t = q.pop(0)               # 디큐
        print(t, end=' ')          # 방문한 정점에서 할 일

        for w in range(1, V+1):    # 인접한 정점 중에서 인큐되지 않은 정점 w가 있다면,
            if adj_m[t][w] == 1 and visited[w] == 0:
                q.append(w)        # w 인큐 + 인큐 표시(visited)
                visited[w] = visited[t] + 1


V, E = map(int, input().split())     # 1번부터 V번까지의 정점, E개의 간선
arr = list(map(int, input().split()))

# 인접 행렬 -------------------------------
adj_m = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1      # 방향이 없는 경우
# 여기까지 인접 행렬 ------------------------

bfs(1, V)
