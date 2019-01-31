# BOJ - 2920
arr = tuple(map(int, input().split()))
ans = 0
for i in range(7):
    if arr[i] < arr[i+1]:
        ans += 1
    else: ans -= 1
if ans > 6: print('ascending')
elif ans < -6: print('descending')
else: print('mixed')
exit()

# BOJ - 10845
from sys import stdin
read = lambda: stdin.readline().rstrip()
q = []
s = 0
for _ in range(int(read())):
    c = tuple(read().split())
    if len(c) == 2:
        q.append(c[1])
        s += 1
    else:
        if c[0] == 'pop':
            if s > 0:
                print(q.pop(0))
                s -= 1
            else:
                print(-1)
        elif c[0] == 'size':
            print(s)
        elif c[0] == 'empty':
            if s > 0: print(0)
            else: print(1)
        elif c[0] == 'front':
            if s > 0: print(q[0])
            else: print(-1)
        else:
            if s > 0: print(q[-1])
            else: print(-1)
"""
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
"""
exit()

# BOJ - 2662
n, m = map(int, input().split())
dp = [[0] * (m+1)]
arr = [[0] * (m+1)]
ans = [0]
for i in range(1, n+1):
    arr.append(tuple(map(int, input().split())))
    t, t_arr = 0, None
    for j in range(i):
        for k in range(1, m+1):
            if t < ans[j] + arr[dp[j][k]+i-j][k] - arr[dp[j][k]][k]:
                t = ans[j] + arr[dp[j][k]+i-j][k] - arr[dp[j][k]][k]
                t_arr = dp[j][:]
                t_arr[k] += i-j
    ans.append(t)
    dp.append(t_arr)
print(ans[-1])
print(*dp[-1][1:])
"""
4 2
1 5 1
2 6 5
3 7 9
4 10 15
"""