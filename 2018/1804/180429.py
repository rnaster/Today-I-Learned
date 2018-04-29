def BOJ1699():
    # BOJ - 1699
    n = int(input())
    dp = [0 for _ in range(n+1)]
    l = []
    i = 1
    while i*i <= n:
        l.append(i)
        i += 1

    if n in l: print(1); quit()

    for j in range(1, n+1):
        dp[j] = j
        for num in l:
            if num*num > j: break
            else:
                dp[j] = min(dp[j], dp[j-num*num] + 1)
    print(dp[-1])

# BOJ - 10250
from sys import stdin, stdout
read = lambda : stdin.readline().rstrip()
write = lambda s: stdout.write(s)
for _ in range(int(read())):
    h, w, n = map(int, read().split())
    q, r = divmod(n, h)
    if r == 0:
        r = h
    else:
        q += 1
    if q < 10:
        s = str(r)+'0'+str(q)
    else:
        s = str(r)+str(q)
    write(s+'\n')


'''
6
6 12 10
30 50 72
6 12 6
6 12 5
6 12 7
6 12 12
'''