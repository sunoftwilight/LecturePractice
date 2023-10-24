# 인접 행렬
#   -. 장점 : 구현이 쉽다
#   -. 단점 : 메모리를 낭비한다 (0도 표시하므로)

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
]


# DFS - stack 버전
def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()

        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)
        # 갈 수 있는 곳을 모두 stack에 추가
        # for next in range(5):
        # ======================= 작은 번호부터 조회할 경우
        for next in range(4, -1, -1):
        # =============================================
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue      # 가장 가까운 반복문으로 되돌아감 (다음 줄인 "if next in visitied"로 가는거 아님)

            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)

    # 출력을 위한 반환
    return visited


print("dfs stack = ", end='')
print(*dfs_stack(0))


# DFS - 재귀 버전
# MAP 크기(길이)를 알 때 append 형식 말고 아래와 같이 사용하면 훨씬 빠르다

visited = [0] * 5
path = []     # 방문 순서 기록


def dfs(now):
    visited[now] = 1       # 현재 지점 방문 표시
    # print(now, end=' ')
    path.append(now)

    # 인접한 노드들을 방문
    for next in range(5):
        if graph[now][next] == 0:
            continue

        if visited[next]:
            continue

        dfs(next)


print("dfs 재귀 = ", end='')
dfs(0)
print(*path)
