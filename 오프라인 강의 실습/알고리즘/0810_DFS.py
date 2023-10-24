'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v):
    # 방문 체크 후, 방문한 적 없다면 하고 싶은 일 수행~
    visited[v] = 1
    print(v,end='')

    for w in range(1, V+1):
        # 인접한 정점 중에서 미방문한 정점(visited[w] == 0)이 있다면,
        # (인접? 같은 행에서 1인 애가 있다면(adj[v][w] == 1) 인접하고 있는 점)
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)   # 재귀


# 인접 행렬
V, E = map(int, input().split())             # 정점 개수, 간선 개수
temp = list(map(int, input().split()))       # 간선의 양 끝지점의 정보 들어옴 (시작점 정보에만 접근할 수 있으면 됨)
adj = [[0] * (V+1) for _ in range(V+1)]      # 인접 행렬 초기화
visited = [0] * (V+1)                        # 방문 기록 (1부터 시작하니깐 V+1)

# 인접 행렬 저장하기
for i in range(E):
    s, e = temp[i*2], temp[i*2+1]     # 간선의 양 끝점 중 시작점에만 접근할 수 있으면 됨
    adj[s][e] = adj[e][s] = 1         # 간선이 1 2를 잇는다면, 행렬의 (1,2)와 (2,1) 좌표에 모두 1 저장

dfs(1)      # 시작 정점 1
