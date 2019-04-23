# programmers - 2017 kakao blind - 캐시
cacheSize = 2
cities = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
def solution(cacheSize, cities):
    if cacheSize == 0: return 5 * len(cities)
    answer = 0
    cache = []
    for city in cities:
        if city.lower() in cache:
            answer += 1
            if len(cache) > 0:
                cache.remove(city.lower())
            cache.append(city.lower())
        else:
            if cacheSize > 0:
                cache.append(city.lower())
                cacheSize -= 1
            else:
                cache.remove(cache[0])
                cache.append(city.lower())
            answer += 5
    return answer
print(solution(cacheSize, cities))
exit()

# BOJ - 1949
import sys
read = lambda: sys.stdin.readline().rstrip()
n = int(read())
arr = tuple(map(int, read().split()))
d = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, read().split())
    d[a].append(b); d[b].append(a)
visit = [0] * (n+1)
dp = [[0] * (n+1) for _ in range(2)]
def func(n):
    visit[n] = 1
    dp[1][n] += arr[n-1]
    for i in d[n]:
        if visit[i] == 0:
            func(i)
            dp[1][n] += dp[0][i]
            dp[0][n] += max(dp[1][i], dp[0][i])
func(1)
print(*dp, sep='\n')
"""
7
1000 3000 4000 1000 2000 2000 7000
1 2
2 3
4 3
4 5
6 2
6 7
"""
sys.exit()

# BOJ - 2533
import sys
read = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000000)
n = int(read())
d = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, read().split())
    d[a].append(b); d[b].append(a)
dp = [[0] * (n+1) for _ in range(2)]
visit = [0] * (n+1)
def func(a):
    visit[a] = 1
    dp[1][a] += 1
    for i in d[a]:
        if visit[i] == 0:
            func(i)
            dp[0][a] += dp[1][i]
            dp[1][a] += min(dp[1][i], dp[0][i])
func(1)
print(min(dp[1][1], dp[0][1]))
"""
7
2 1
3 2
4 3
5 4
6 5
7 6


8
4 8
1 2
1 3
1 4
2 5
2 6
4 7

2
2 1
"""
exit()

# BOJ - 1541
s = '('+input().replace('-', ')-(')+')'
ans = ''
for i in range(len(s)):
    if s[i] == '0' and ans[-1] in ['(', '-', '+']: continue
    ans += s[i]
print(eval(ans))
"""
0005500-0050+0040
0+0
0
"""