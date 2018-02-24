# BOJ - 1110
n = int(input())
ans = 0
a = n
while True:
    q = a // 10
    r = a % 10
    a = r * 10 + (q + r) % 10
    ans += 1
    if a == n: print(ans);quit()