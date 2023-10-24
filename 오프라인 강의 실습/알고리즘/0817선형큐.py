# Queue는 초기 크기를 크게 잡아야 한다

SIZE = 100
Q = [0] * SIZE
front = rear = -1

# enQueue
rear += 1
Q[rear] = 1
rear += 1
Q[rear] = 2

# peek
print(f'peek : {Q[front + 1]}')

# deQueue
while front != rear:
    front += 1
    print(Q[front])

print(front, rear)
print(Q)


# list로 Queue 만들기
Q = []

# enQ
Q.append(1)
Q.append(2)
Q.append(3)

# peek
print(f'peek : {Q[0]}')

# deQ
while Q:   # Que가 비어있지 않은 동안
    print(Q.pop(0))    # 0번째 인덱스에 저장된 값을 Pop (O(n) -> 시간 많이 걸릴수도)
    # pop(0) 대신 popleft 사용 => O(1)의 시간복잡도 (good!)


# import
from collections import deque
Q = deque()

# enQ
Q.append(1)
Q.append(2)
Q.append(3)

# peek
