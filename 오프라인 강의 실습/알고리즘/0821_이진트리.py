"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

- * - * - * - * -
3열짜리 2차원 배열을 만들어서
0열 - 왼쪽 자식, 1열 - 오른쪽 자식, 2열 - 부모 저장

# 초기화 상태
 0 1 2
0ㅁㅁㅁ
1ㅁㅁㅁ
2ㅁㅁㅁ
3ㅁㅁㅁ
4ㅁㅁㅁ
5ㅁㅁㅁ
... (생략)

# 넣으면
   0 1 2
0 ㅁ ㅁ ㅁ
1  2 3 ㅁ
2  4 ㅁ 1
3  5 6 1
4  ㅁㅁ 2
5  ㅁㅁ 3
6  ㅁㅁ 3
... (생략)
"""


def preorder(node):
    if node:
        print(node, end=' ')
        preorder(tree[node][0])    # node의 왼쪽 자식
        preorder(tree[node][1])    # node의 오른쪽 자식


V = int(input())
E = V - 1

# 인접 리스트 (연결 리스트와 매우 유사한 형태로 사용 가능!!)
tree = [[0] * 3 for _ in range(V+1)]
temp = list(map(int, input().split()))

for i in range(E):
    p = temp[i * 2]
    c = temp[i * 2 + 1]

    if tree[p][0] == 0:
        tree[p][0] = c

    else:
        tree[p][1] = c

    tree[c][2] = p

# root 찾기
root = 1

while tree[root][2] != 0:   # tree[root][2]는 부모 노드
    root += 1

preorder(root)
