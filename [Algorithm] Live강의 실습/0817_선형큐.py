def enQ(data):
    global rear
    if rear == Qsize - 1:  # 큐가 가득 차면
        print('Q is full')
    else:
        rear += 1
        Q[rear] = data


def deQ():
    global front

    if front == rear:  # 큐가 비어있으면
        print('Q is empty')
    else:
        front += 1
        return Q[front]


Qsize = 3
Q = [0] * Qsize
rear = front = -1

enQ(1)
enQ(2)
rear += 1
Q[rear] = 3   # enqueue(3)과 동일

while front != rear:
    front += 1
    print(Q[front])

print(deQ())
print(deQ())
print(deQ())