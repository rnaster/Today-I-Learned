# BOJ - 2667
n = int(input())

MAP = []
cache = [[1 for _ in range(n)] for _ in range(n)]
for _ in range(n):
	MAP.append(input())

q = []
ans = []
def BFS():
	global q, MAP, cache, ans
	ans.append(0)
	while q:
		a, b = q.pop(0)
		for x, y in ((0, 1), (-1, 0), (0, -1), (1, 0)):
			if 0 <= a+x < n and 0<= b+y < n:
				if MAP[a+x][b+y] == '1' and cache[a+x][b+y]:
					q.append((a+x, b+y))
					cache[a+x][b+y] = 0
		ans[-1] += 1

def main(m, n):
	global q, cache, MAP
	if MAP[m][n] == '1' and cache[m][n]:
		q.append((m, n))
		cache[m][n] = 0
		BFS()

for i in range(n):
	for j in range(n):
		main(i, j)

print(len(ans))
for i in sorted(ans):
	print(i)
'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''