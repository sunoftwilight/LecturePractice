def f(i, N):
    if i == N:                    # 순열 완성 (모든 탐색 완료)
        print(p)                  # 가능한 모든 순열 출력
        return

    else:                         # p[i]에 들어갈 숫자를 결정 (주어진 card를 나열)
        for j in range(N):
            # 아직 사용하지 않은 카드(used[j] == 0)라면 사용
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1       # 사용했으니 1로 변경 (사용 표시)
                f(i+1, N)
                used[j] = 0       # 다음 재귀 다녀와서는 다시 쓸 수 있도록 변경 (다른 경우의 수 찾아야하니까)


card = list(map(int, input()))    # 주어진 숫자 카드
used = [0] * 6                    # 카드 사용 여부 표시
p = [0] * 6

f(0, 6)
