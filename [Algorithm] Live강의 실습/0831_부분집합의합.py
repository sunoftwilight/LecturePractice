def subset(i, N):                    # 저장할 원소 i, 전체 원소 개수 N
    if i == N:                       # 탐색 끝났으면
        s = 0                        # 원소의 합 s 초기화
        for j in range(N):
            if bit[j]:               # 선택한 원소라면
                s += arr[j]          # 해당 원소 더하기

        if s == 0:                   # 연산 끝났을 때 합이 0이면
            for j in range(N):
                if bit[j]:           # 선택한 원소들만 출력
                    print(arr[j], end=' ')
            print()

    else:
        bit[i] = 1                   # 해당 원소 선택 표시 하고
        subset(i+1, N)               # 다음 원소를 선택
        bit[i] = 0                   # 위의 재귀 끝났다면 0으로 만들어서 선택 초기화 해주고
        subset(i+1, N)               # 해당 원소 선택하지 않은 경우에 대해 다음 원소 선택


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0] * N

subset(0, N)
