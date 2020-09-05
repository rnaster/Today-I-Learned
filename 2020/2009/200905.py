# BOJ - 1339
n = int(input())
arr = [[0] * 11 for _ in range(26)]
l = [[*map(lambda x: ord(x)-65, input())] for _ in range(n)]
for ll in l:
    for a, b in enumerate(ll[::-1], 1):
        arr[b][-a] += 1
for a in arr:
    for i in range(1, 11):
        p, q = divmod(a[-i], 10)
        a[-i-1] += p
        a[-i] = q
lll = [-1] * 26
t = 9
for i, _ in sorted(enumerate(arr), reverse=True, key=lambda x: x[1]):
    lll[i] = t
    t -= 1
ans = 0
for ll in l:
    a = 1
    for b in ll[::-1]:
        ans += lll[b] * a
        a *= 10
print(ans)
"""
2
GCF
ACDEB

10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB
"""