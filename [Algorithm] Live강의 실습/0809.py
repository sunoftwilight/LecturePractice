stack = [0] * 10
top = -1

top += 1
stack[top] = 1       # push(1)

top += 1
stack[top] = 2       # push(2)

top += 1
stack[top] = 3       # push(3)

print(stack[top])    # pop()
top -= 1

top -= 1
print(stack[top+1])  # pop()

# 두 개의 pop은 인덱스 처리를 먼저하느냐 나중에 하느냐의 차이일 뿐, 기능은 동일!
