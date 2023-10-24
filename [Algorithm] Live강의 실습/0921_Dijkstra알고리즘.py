'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

# 최단 거리 문제 유형
# 1. 특정 지점 -> 도착 지점까리의 최단거리 : 다익스트라
# 2. 가중치에 음수가 포함 ? : 벨만포드
# 3. 여러 지점 -> 여러 지점까지의 최단 거리 : 플로이드-워샬
#      -. 얘도 여러 지점 모두 다익스트라 돌려서 풀 수 있음 But, 시간 복잡도 계산 잘 해야함

# 내가 갈 수 있는 경로 중 누적 거리가 제일 짧은 것부터 고르자!
import heapq

# 입력
n, m = map(int, input().split())

# 인접 리스트
graph = [[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])

# 1. 누적 거리를 계속 저장
INF = int(1e9)       # 최대값으로 1억 - 보통 매우 큰 수를 선언
distance = [INF] * n


def dijkstra(start):
    # 2. 우선 순위 큐
    pq = []
    # 출발점 초기화 - (누적 거리, 정점) 형태로 삽입
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 시점에서 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            pass

        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node로 가기 위한 누적 거리
            # cost : 현재 node - next_node 연결 간선의 weight
            # diist : 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크네? -> 다음 반복으로 넘어가
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


dijkstra(0)
print(distance)