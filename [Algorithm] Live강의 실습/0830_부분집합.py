# 모든 부분집합을 구하기

a = [3, 6, 7, 1, 5, 4]
N = 6

for i in range(1 << N):
    subset1 = []                  # 부분집합에 선택된 요소로만 이루어진 그룹
    subset2 = []                  # 부분집합에 선택되지 않은 나머지 요소로만 이루어진 그룹
    for j in range(N):
        if i & (1 << j):          # j번 비트가 0이 아니면 (= 1이면)
            subset1.append(a[j])

        else:                     # j번 비트가 0이면
            subset2.append(a[j])

    print(subset1, subset2)
print()


# 공집합을 제외한 모든 부분집합을 구하기

a = [3, 6, 7, 1, 5, 4]
N = 6

for i in range(1, (1 << N) - 1):
    group1 = []                  # 부분집합에 선택된 요소로만 이루어진 그룹
    group2 = []                  # 부분집합에 선택되지 않은 나머지 요소로만 이루어진 그룹
    for j in range(N):
        if i & (1 << j):          # j번 비트가 0이 아니면 (= 1이면)
            group1.append(a[j])

        else:                     # j번 비트가 0이면
            group2.append(a[j])

    print(group1, group2)
print()


# 공집합을 제외한 모든 부분집합을 구하기 (중복 제외)

a = [1, 2, 3, 4]
N = 4

for i in range(1, 1 << (N - 1)):       # 1 << (N - 1) == (1 << N) // 2
                                       # : 위의 코드는 중복이 생기므로, 중복 제외하기 위해 반만 보기
    group1 = []                        # 부분집합에 선택된 요소로만 이루어진 그룹
    group2 = []                        # 부분집합에 선택되지 않은 나머지 요소로만 이루어진 그룹
    for j in range(N):
        if i & (1 << j):               # j번 비트가 0이 아니면 (= 1이면)
            group1.append(a[j])

        else:                          # j번 비트가 0이면
            group2.append(a[j])

    print(group1, group2)
print()
