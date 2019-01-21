# BOJ - 1076
d = {'black':(0, 1),'brown':(1,10),'red':(2, 100),'orange':(3, 1000),
     'yellow':(4, 10000), 'green':(5, 100000), 'blue':(6,1000000),
     'violet':(7, 10000000), 'grey':(8, 100000000),
     'white':(9, 1000000000)}
print((d[input()][0] * 10 + d[input()][0])*d[input()][1])
"""
yellow
violet
red
"""
exit()

# BOJ - 2909
c, k = map(int, input().split())
k = 10 ** k
a, b = divmod(c, k)
if b >= k / 2: print((a+1)*k)
else: print(a * k)
"""
184 1
185 1

"""
exit()

# BOJ - 5582
s1, s2 = input(), input()
ss1, ss2 = len(s1), len(s2)
dp = [[0] * (ss1+1) for _ in range(ss2+1)]
ans = 0
for i in range(1, ss2+1):
    for j in range(1, ss1+1):
        if s1[j-1] == s2[i-1]:
            dp[i][j] += dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])
print(ans)
"""
ABRACADABRA
ECADADABRBCRDARA

ABCAB
BABDAB
"""