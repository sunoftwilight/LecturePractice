'''
서울(0), 천안(1), 원주(2), 논산(3), 대전(4),
대구(5), 강릉(6), 광주(7), 부산(8), 포항(9)
'''
'''
9 14
0 1 12
0 2 15
1 3 4
1 4 10
2 5 7
2 6 21
3 4 3
3 7 13
4 5 10
5 8 9
5 9 19
6 9 25
7 8 15
8 9 5
'''

def dijkstra(s):
    # 시작점 설정
    D[s] = 0

    # 정점의 갯수만큼 선택하기
    for i in range(V+1):
        # 가중치 최소값 찾기
        min_v = 987654321
        for j in range(V+1):
            if visited[j] == 0 and D[j] < min_v:
                min_v = D[j]
                v = j                           # 가중치가 최소인 정점 선택

        # 방문 처리 (선택) + 하고싶은 일
        visited[v] = 1

        # 인접 정점의 가중치 갱신
        for w in range(V+1):
            if adj[v][w] and not visited[w]:
                if D[w] > D[v] + adj[v][w]:     # prim이랑은 여기랑
                    D[w] = D[v] + adj[v][w]     # 여기만 달라짐 ... ㅋ


V, E = map(int, input().split())                # 0부터 마지막 정점수, 간선 수
adj = [[0] * (V + 1) for _ in range(V + 1)]     # 인접 행렬
visited = [0] * (V + 1)                         # 방문 체크
D = [987654321] * (V + 1)                       # 가중치

# 인접행렬 만들기
for i in range(E):
    s, e, w = map(int, input().split())         # 시작, 끝, 가중치
    adj[s][e] = adj[e][s] = w                   # 무향 그래프

dijkstra(0)
print(D)
# MST 가중치의 합
print(sum(D))