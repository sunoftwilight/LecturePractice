graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
]


path = []
# BFS
def bfs(start):
    visited = [0] * 5

    # 먼저 방문했던 것을 먼저 처리해야 한다 = queue
    queue = [start]
    visited[start] = 1

    while queue:
        # queue의 맨 앞 요소를 꺼냄
        now = queue.pop(0)
        # print(now, end=' ')
        path.append(now)

        # 인접합 노드들을 queue에 추가
        for next in range(5):
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue  # 가장 가까운 반복문으로 되돌아감 (다음 줄인 "if next in visitied"로 가는거 아님)

            # 방문한 지점이라면 queue에 추가하지 않음
            if visited[next]:
                continue

            queue.append(next)
            # bfs이므로 여기서 방문체크를 해줘도 상관 없음
            visited[next] = 1


print("bfs = ", end='')
bfs(0)
print(*path)
