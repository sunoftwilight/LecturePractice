# key가 있으면 1, 없으면 0을 리턴하는 함수
def f(i, N, key, arr):           # 현재 상태 i, 목표 N, 찾고자 하는 원소 key
    if i == N:
        return 0                 # key가 없는 경우

    elif arr[i] == key:
        return 1                 # key를 발견했으면 더 이상 탐색 X

    else:
        f(i+1, N, key, arr)      # 이번 탐색에 key 없으면 다음 탐색으로


N = 5
A = [1, 2, 3, 4, 5]
key = 3

print(f(0, N, key, A))
