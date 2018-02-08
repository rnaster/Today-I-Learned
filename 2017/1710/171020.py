# BOJ - 2352
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n = int(read())
tp = tuple(map(int, read().split()))
dp = array('H', [tp[0]])
ans = 1
for i in range(n):
    if tp[i] > dp[-1]: dp.append(tp[i]); ans += 1
    else:
        bot, top = 0, len(dp)-1
        while bot < top:
            mid = (bot + top) // 2
            if dp[mid] >= tp[i]: top = mid
            else: bot = mid + 1
        dp[top] = tp[i]
print(ans)