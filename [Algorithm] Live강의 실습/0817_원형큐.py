def enq(data):
    global rear
    global front

    if (rear + 1) % cQsize == front:
        front = (front + 1) % cQsize
    rear = (rear + 1) % cQsize
    cQ[rear] = data


def deq(data):
    global front

    front = (front + 1) % cQsize
    return cQ[front]


cQsize = 4
cQ = [0] * cQsize
front = rear = 0
