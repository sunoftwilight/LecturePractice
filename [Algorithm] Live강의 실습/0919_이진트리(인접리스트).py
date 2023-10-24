arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]

nodes = [[] for i in range(0, 14)]

for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].append(nodes[childNode])

# 자식이 더 이상 없음을 표현하기 위해 None 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)


def preorder(nodeNumber):
    if nodeNumber == None:
        return

    # 전위 순회 출력 위치
    print(nodeNumber, end=' ')
    preorder(nodes[nodeNumber][0])
    # 중위 순회 출력 위치
    # print(nodeNumber, end=' ')
    preorder(nodes[nodeNumber][1])
    # 후위 순회 출력 위치
    # print(nodeNumber, end=' ')


preorder(1)