# BOJ - 2602
m = input()
s1 = 'X' + input()
s2 = 'X' + input()
dp1 = [[0 for _ in s1] for _ in m]
dp2 = [[0 for _ in s2] for _ in m]
s_len = len(s1)
ans = 0
for i in range(1, s_len):
    if s1[i] == m[0]:
        dp1[0][i] = 1
        ans += 1
    if s2[i] == m[0]:
        dp2[0][i] = 1
        ans += 1
idx = 1
for mm in m[1:]:
    s1_mem, s2_mem, ans = 0, 0, 0
    for i in range(1, s_len):
        s1_mem += dp2[idx-1][i-1]
        s2_mem += dp1[idx-1][i-1]
        if mm == s1[i]:
            dp1[idx][i] = s1_mem
            ans += s1_mem
        if mm == s2[i]:
            dp2[idx][i] = s2_mem
            ans += s2_mem
    idx += 1
print(*dp1, sep='\n')
print()
print(*dp2, sep='\n')
print(sum(dp2[-1]) + sum(dp1[-1]))
print(ans)
"""
RGS
RINGSR
GRGGNS
"""