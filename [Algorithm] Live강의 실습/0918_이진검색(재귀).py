# 이진 검색 - 재귀 호출 활용
arr = [2, 4, 7, 9, 11, 19, 23]

# 문제에서 데이터가 정렬된 상태라는 조건 X - 반드시 정렬 먼저 수행해야 함!!!!
arr.sort()


def binarySearch(low, high, target):
    # 기저 조건 : 언제까지 재귀 호출을 반복할 것인가?
    # low [                            ] high
    #      ↓ 탐색 1회 수행 후 ↓
    # low [                ] high
    # 함수 한 번 호출 때마다 범위가 좁혀짐에 따라 low, high 변수가 변경되어 사용됨

    # low > high 라면 데이터 내에서 찾으려는 값을 찾지 못한 경우
    if low > high:
        return -1

    mid = (low + high) // 2

    # 1. 가운데 값이 정답인 경우
    if target == arr[mid]:
        return mid

    # 2. 가운데 값이 정답보다 작은 경우 (오른쪽 영역에 정답이 포함)
    elif arr[mid] < target:
        return binarySearch(mid + 1, high, target)

    # 3. 가운데 값이 정답보다 큰 경우 (왼쪽 영역에 정답이 포함)
    else:
        return binarySearch(low, mid - 1, target)


print(f'9 = {binarySearch(0, len(arr) - 1, 9)}')
print(f'4 = {binarySearch(0, len(arr) - 1, 4)}')
print(f'10 = {binarySearch(0, len(arr) - 1, 10)}')
