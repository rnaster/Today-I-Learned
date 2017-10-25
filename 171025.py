def foo():
    # BOJ - 11047
    from sys import stdin
    from array import array
    read = lambda: stdin.readline().rstrip()
    n, k = map(int, read().split())
    coins = array('L', [])
    for _ in range(n):
        coin = int(read())
        if k >= coin:
            coins.append(coin)
        else: break
    ans = 0
    while k:
        coin = coins.pop()
        ans += k // coin
        k = k % coin
    print(ans)

# BOJ - 1660
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n = int(read())
dp = array('L', [0] + [n+1 for _ in range(n)])
arr = array('L', [])
s = lambda x: x*(x+1)*(x+2)//6
for i in range(1, 121):
    if s(i) < n:
        arr.append(s(i))
    else: break
for c in arr:
    for i in range(c, n+1):
        dp[i] = min(dp[i], dp[i-c]+1)
print(dp[-1])

'''
n = int(read())
arr = array('L', [])
s = lambda x: x*(x+1)*(x+2)//6
for i in range(1, 121):
    if s(i) < n:
        arr.append(s(i))
    else: break
ans = 0
while n:
    num = arr.pop()
    tmp = n // num
    if tmp: print(tmp, num, '*')
    ans += tmp
    n = n % num
print(ans)
'''
