# BOJ - 11058
n = int(input())
if n < 7: print(n); exit()
a, b, c, d, e = 2, 3, 4, 5, 6
for _ in range(n-6):
    a, b, c, d, e = b, c, d, e, max(b * 3, a * 4)
print(e)
