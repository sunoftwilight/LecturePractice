from collections import deque   # 평가 때는 사용 금지


q = deque()   # q: deque([1, 2, 3])

q.append(1)
q.append(2)
q.append(3)

print(q.popleft())
print(q.popleft())
print(q.popleft())  # pop(0)와의 차이? popleft가 내부적으로 매우 빠름