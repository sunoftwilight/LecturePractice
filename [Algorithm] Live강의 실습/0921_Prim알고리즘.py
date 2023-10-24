'''
# V, E 개수
# start, end, weight
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 우선순위 큐 활용해야 함
# 우선순위 큐 - 원소를 push하면 내부적으로 우선순위에 따라 자동으로 오름차순 정렬됨
#           - 원소를 pop하면 큐의 가장 앞에서부터 빼옴
#           - 튜플로 입력 시 가장 앞의 원소를 기준으로 정렬되므로 기준점을 가장 앞에 두고 push 해야 함!
import heapq


def prim(start):            # 시작 정점 지정 필요
    heap = []

    # MST에 포함된 V인지에 대한 여부 (= visited)
    MST = [0] * V

    # 가중치, 정점 정보
    heapq.heappush(heap, (0, start))

    # 누적합
    sum_weight = 0

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue

        # 방문체크
        MST[v] = 1

        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight


V, E = map(int, input().split())

# 인접 행렬 - 인접 리스트가 더 좋지만 N이 그렇게 많지 않으니 인접 행렬도 괜찮음!
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    # 무향 그래프는 양 방향으로 움직일 수 있어야 함 -> graph[f][t] = graph[t][f] = w
    # 유향 그래프라면 갈 수 있는 방향에 대해서만 -> graph[f][t] = w
    graph[f][t] = w
    graph[t][f] = w

result = prim(0)
print(f'최소 비용 = {result}')
