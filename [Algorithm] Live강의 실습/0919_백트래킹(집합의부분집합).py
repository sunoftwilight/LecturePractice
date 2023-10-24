# {1, 2, 3} 집합에서 3개의 숫자를 선택하는 기본 예제

arr = [i for i in range(1, 4)]
path = [0] * 3


def backtracking(cnt):
    # 재귀함수이므로 기저 조건 설정 !!
    # 숫자 3개를 선택하면 종료
    if cnt == 3:
        print(*path)
        return

    for num in arr:
        # 가지 치기 - 중복 숫자 제거
        if num in path:
            continue

        # 들어가기 전 로직 - 경로 저장
        path[cnt] = num

        # 다음 재귀 함수 호출
        backtracking(cnt + 1)

        # 돌아와서 할 로직 - 초기화
        path[cnt] = 0


backtracking(0)
