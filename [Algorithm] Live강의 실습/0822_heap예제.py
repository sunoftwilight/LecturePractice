def deq():
    global last

    tmp = heap[1]          # 루트 백업
    heap[1] = heap[last]   # 삭제할 노드의 키를 루트에 복사
    last -= 1              # 마지막 노드 삭제

    p = 1                  # 루트에 옮긴 값을 자식과 비교
    c = p * 2              # 왼쪽 자식

    while c <= last:       # 자식이 하나라도 존재한다면 (완전 이진 트리이므로 왼쪽자식이 없이
                           # 오른쪽 자식이 있는 경우는 X -> 자식 존재 여부는 왼쪽 자식의 유무로 알 수 있음!!
                           # 오른쪽도 있는지 왼쪽만 있는지는 몰랑)
        if c + 1 <= last and heap[c] < heap[c + 1]:       # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1                                        # 오른쪽 자식이랑 비교해야하니깐 c를 오른쪽 자식으로 교체~

        if heap[p] < heap[c]:     # 자식이 더 크면 최대 힙 규칙을 위배하니까
            heap[p], heap[c] = heap[c], heap[p]    # 둘이 자리 바꿔
            p = c             # 자식을 새로운 부모로 갱신
            c = p * 2         # 왼쪽 자식 번호를 계산

        else:                 # 부모가 더 크면
            break             # 비교 중단

    return tmp


heap = [0] * 100
last = 0
