# 최소 힙만 지원 (최대 힙은 - 붙이기)
import heapq

heap = [7, 2, 5, 3, 4, 6]
heapq.heapify(heap)
print(heap)       # [2, 3, 5, 7, 4, 6]

heapq.heappush(heap, 1)
print(heap)       # [1, 3, 2, 7, 4, 6, 5]

while heap:
    print(heapq.heappop(heap), end=' ')  # 1 2 3 4 5 6 7 (힙 sort)
print()

#####################

temp = [7, 2, 5, 3, 4, 6]
heap2 = []

for i in range(len(temp)):
    heapq.heappush(heap2, -temp[i])   # 최대 힙은 음수(-) 붙여서 정렬하면 됨!!!
print(heap2)     # [-7, -4, -6, -2, -3, -5]   (절댓값이 큰 순서대로 정렬됨!
# -> 정렬 후 음수 다시 붙여서 정렬하면 완벽한 최대 힙)
while heap2:
    print(heapq.heappop(heap2) * -1, end=' ')    # 7 6 5 4 3 2
