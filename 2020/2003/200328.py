# BOJ - 5397
import sys
read = sys.stdin.readline
for _ in range(int(input())):
    s = read().strip()
    arr = [''] * (len(s) + 1)
    pre = [-1] * (len(s) + 1)
    nxt = [-1] * (len(s) + 1)
    unused = 1
    cur = 0
    for ss in s:
        if ss == '<':
            cur = max(pre[cur], 0)
        elif ss == '>':
            if nxt[cur] > -1: cur = nxt[cur]
        elif ss == '-':
            if cur == 0: continue
            nxt[pre[cur]] = nxt[cur]
            if nxt[cur] > -1: pre[nxt[cur]] = pre[cur]
            cur = max(pre[cur], 0)
        else:
            arr[unused] = ss
            pre[unused] = cur
            nxt[unused] = nxt[cur]
            if nxt[cur] > -1: pre[nxt[cur]] = unused
            nxt[cur] = cur = unused
            unused += 1
    i = 0
    ans = []
    while nxt[i] > -1:
        i = nxt[i]
        ans.append(arr[i])
    print(''.join(ans))
"""
3
<<BP<A>>Cd-
ThIsIsS3Cr3t
-p-p<-kk
"""
exit()

# BOJ - 2011
n = input()
if n[0] == '0': print(0); quit()
if len(n) == 1: print(1); quit()
dp1 = 1
if n[:2] in ['10', '20']:
    dp2 = 1
elif '11' <= n[:2] <= '26':
    dp2 = 2
elif n[1] != '0':
    dp2 = 1
else:
    dp2 = 0
for i in range(2, len(n)):
    temp = 0
    if n[i] != '0': temp += dp2
    if '10' <= n[i - 1:i + 1] <= '26': temp += dp1
    dp1, dp2 = dp2, temp % 1_000_000
print(dp2)
"""
25114
1070
1002
99
999
1203
"""
