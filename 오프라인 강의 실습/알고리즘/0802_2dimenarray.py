'''
3 x 4 행렬
1  2  3  4
5  6  7  8
9 10 11 12
'''

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# arr = [list(map(int, input())) for _ in range(N)]   # 숫자가 띄어쓰기 없이 입력된 경우

# 행 우선
for i in range(N):
    for j in range(M):
        print(arr[i][j])


# 열 우선
for j in range(M):
    for i in range(N):
        print(arr[i][j])


# 열 우선   - 정방행렬 (N * N)에서만 사용 가능
for i in range(N):
    for j in range(M):
        print(arr[j][i])
# 일반 2차원 행렬은 N과 M의 길이가 다르므로 range out 오류 발생


# 행의 합
sum_all = 0
for i in range(N):
    sum_row = 0
    for j in range(M):
        sum_all += arr[i][j]
        sum_row += arr[i][j]
    # 행의 합은 여기서 작업
    print(sum_row)
print(sum_all)


# 열의 합
sum_all = 0
for j in range(M):
    sum_col = 0
    for i in range(N):
        sum_all += arr[i][j]
        sum_col += arr[i][j]
    # 열의 합은 여기서 작업
    print(sum_col)
print(sum_all)
