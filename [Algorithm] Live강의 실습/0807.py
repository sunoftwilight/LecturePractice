s = 'Reverse this strings'
s_lst = list(s)
N = len(s)

for i in range(N//2):
	s_lst[i], s_lst[N-1-i] = s_lst[N-1-i], s_lst[i]

reverse_s = ''.join(s_lst)
print(reverse_s)


def atoi(s):
	i = 0
	for x in s:
		i = i * 10 + ord(x) - ord('0')
	return i

s = '123'
a = atoi(s)
print(a + 1)   # a가 숫자로 변환되었다면 + 1 연산이 가능할 것


