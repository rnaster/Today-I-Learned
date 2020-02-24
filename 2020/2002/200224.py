# BOJ - 8980
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [[] for _ in range(n+1)]
for _ in range(int(read())):
    a, b, c = map(int, read().split())
    arr[a].append((b, c))
cap = 0
ans = 0
l = [0] * (n+1)
for i in range(1, n+1):
    ans += l[i]
    cap -= l[i]
    for b, c in sorted(arr[i]):
        if m >= cap + c:
            cap += c
            l[b] += c
        else:
            d = min(m - sum(l[i+1:b+1]), c)
            l[b] += d
            d, cap = max(0, cap + d - m), min(m, cap + d)
            for j in range(n, b, -1):
                if d == 0: break
                if l[j] == 0: continue
                dd = min(d, l[j])
                l[j] -= dd
                d -= dd
print(ans)
"""
4 40
6
3 4 20
1 2 10
1 3 20
1 4 30
2 3 10
2 4 20

4 5
4
3 4 1
2 3 4
1 2 1
1 4 4
"""