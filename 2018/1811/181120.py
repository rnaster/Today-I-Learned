# BOJ - 2033
n = int(input())
k = 10
while True:
    if n < k: print(n);exit()
    else:
        if n % k >= 5 * (k // 10): n = (n - n % k) + k; k *= 10
        else: n -= n % k; k *= 10

