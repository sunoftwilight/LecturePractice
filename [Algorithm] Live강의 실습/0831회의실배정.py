N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]

meet = []

for i in range(N):
    meet.append([a[i*2], a[i*2+1]])      # 회의 시작시간, 종료시간

meet.sort(key=lambda x: x[1])            # 종료 시간(리스트의 첫번째 인덱스 값)을 기준으로 오름차순 sorting
meet = [[0, 0]] + meet

S = []                                   # 회의실이 초기에 비어있는 상태가 아니라면, S = [1], j = 1로 시작
j = 0

for i in range(1, N+1):
    if meet[i][0] >= meet[j][1]:         # si >= fj
        S.append(i)
        j = i

print(S)
