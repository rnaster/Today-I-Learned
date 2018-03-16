# BOJ - 1011
def func(t):
    dp_len = 1
    dp = 0
    n = 1
    while True:
        dp += 1
        dp_len += n
        if dp_len > t: return dp
        dp += 1
        dp_len += n
        if dp_len > t: return dp
        n += 1
    return dp
for _ in range(int(input())):
    a, b = map(int, input().split())
    t = b - a
    print(func(t))
'''
3
0 3
1 5
45 50
'''