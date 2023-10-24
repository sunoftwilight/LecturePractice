# 이진 검색 - 반복문
arr = [2, 4, 7, 9, 11, 19, 23]

# 문제에서 데이터가 정렬된 상태라는 조건 X - 반드시 정렬 먼저 수행해야 함!!!!
arr.sort()


def binarySearch(target):
    # 최소, 최대값의 index
    low = 0
    high = len(arr) - 1

    # 2, 4, 7 / 9 / 11, 19, 23

    # low > high라면 데이터 내에서 찾으려는 값을 찾지 못한 경우
    # (Ex> 10 -> low와 high가 같아지게 됨)
    while low <= high:
        mid = (low + high) // 2

        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            return mid

        # 2. 가운데 값이 정답보다 작은 경우 (오른쪽 영역에 정답이 포함)
        elif arr[mid] < target:
            low = mid + 1

        # 3. 가운데 값이 정답보다 큰 경우 (왼쪽 영역에 정답이 포함)
        else:
            high = mid - 1

    return "해당 데이터는 없습니다."


print(f'9 = {binarySearch(9)}')
print(f'4 = {binarySearch(4)}')
print(f'10 = {binarySearch(10)}')
