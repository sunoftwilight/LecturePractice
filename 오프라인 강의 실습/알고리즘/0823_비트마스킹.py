visited1 = [1, 0, 0, 0, 1]
visited2 = 0b10001

print(visited2)     # 17 (= 10001(2) : 0번, 4번 방문)
# - * - * - * - * - * - * - * - * - * - * - * - * - * - * - #
visited = 0

# 원소 추가
visited = visited | 1 << 3    # visited(= 0)와 1을 3번 옮긴 애(= 0001 -> 1000)를 연산
print(visited, bin(visited))   # 8 0b1000

# 원소 제거
visited = visited & ~(1 << 3)
print(visited, bin(visited))   # 0 0b0


# 원소 조회
visited = visited | 1 << 3
print(visited & (1 << 3))      # 8
visited = visited | ~(1 << 3)
print(visited & ~(1 << 3))     # -9

# 원소 토글
visited = visited ^ (1 << 3)
print(visited, bin(visited))   # -9 -0b1001
visited = visited ^ ~(1 << 3)
print(visited, bin(visited))   # 0 0b0
