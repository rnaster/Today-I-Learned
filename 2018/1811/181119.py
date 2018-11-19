# BOJ - 2798
n, m = map(int, input().split())
tp = tuple(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(n):
        if i < j:
            for k in range(n):
                if k != i and k != j:
                    if tp[i] + tp[j] + tp[k] < m:
                        ans = max(ans, tp[i] + tp[j] + tp[k])
                    elif tp[i] + tp[j] + tp[k] == m:
                        print(m);exit()
print(ans)
"""
5 21
5 6 7 8 9
"""