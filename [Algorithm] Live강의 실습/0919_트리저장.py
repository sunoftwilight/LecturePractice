arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]

# 0. 이진 트리 저장 ======================================
#   -. 일차원 배열 저장
#       * 2n + 1 = 왼쪽 자식의 idx
#       * 2n + 2 = 오른쪽 자식의 idx


# 1. 인접 리스트로 저장 ===================================
# 꽤나 복잡함 - 개발용 (코테용 X)
# 대량의 데이터를 다룰 때 사용
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # 삽입 함수
    def insert(self, childNode):
        # 왼쪽 자식이 없네?
        if not self.left:
            self.left = childNode
            return

        # 왼쪽은 있고 오른쪽 자식이 없네?
        # (elif가 아니지만, 왼쪽 자식이 없는 경우는 위의 조건에서 걸리고 함수 끝나므로)
        if not self.right:
            self.right = childNode
            return

        return

    # 순회
    def preorder(self):
        # 아무것도 없는 트리를 조회할 때
        if self != None:
            # 전위 순회 시 print 위치
            # print(self.value, end=' ')

            # 왼쪽이 있다면 왼쪽 자식 조회
            if self.left:
                self.left.preorder()

            # 중위 순회 시 print 위치
            # print(self.value, end=' ')

            # 오른쪽 자식이 있다면 오른쪽 자식 조회
            if self.right:
                self.right.preorder()

            # 중위 순회 시 print 위치
            # print(self.value, end=' ')


# 이진 트리 만들기
nodes = [TreeNode(i) for i in range(1, 7)]

for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].insert(nodes[childNode])

test = 1

# 2. 연결 리스트로 저장 ====================================