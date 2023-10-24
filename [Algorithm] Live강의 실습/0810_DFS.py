'''
7 8                                # 마지막 정점, 간선의 개수 (V E)
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7    # 간선을 이루는 좌표쌍 순서대로 나열 (v1, w1), (v2, w2), ...
'''

# 저장 방식 : 인접 행렬
# => (1 2)가 v1, w1으로 주어졌으니, (V+1) * (V+1) 행렬 만든 후, (v1, w1) & (w1, v1) 좌표에 1 채우기

# 2차원 배열 : 인접 리스트
# 0은 없으니 0번째 행은 비우고
# 1은 2, 3이랑 연결되어 있으니 1번째 행에 2, 3 저장
# 2는 1, 4, 5랑 연결되어 있으니 2번째 행에 1, 4, 5 저장

def dfs(n, V, adj_m):
    stack = []          # stack 생성
    visited = []        # visited 생성
    visited[n] = 1      # 시작점 방문 표시

    print(n)            # do[n]

    while True:         # 탐색을 할거다
        for w in range(1, V):         # 현재 정점 n에 인접해 있고 방문한적 없는 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)       # push(v), v = w
                n = w
                print(n)              # do(w)
                visited[n] = 1        # w 방문 표시
                break                 # for w에 대한 break (n에 인접한 w 찾은 경우)

            else:
                if stack:             # 스택에 지나온 정점이 남아있다면
                    n = stack.pop()   # pop()해서 다시 다른 w를 찾을 n을 준비

                else:                 # stack이 비어있다면
                    break             # while True에 대한 break (전체 탐색 끝!)


V, E = map(int, input().split())              # 1번부터 N번까지
arr = list(map(int, input().split()))
adj_m = [[0] * (V + 1) for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

