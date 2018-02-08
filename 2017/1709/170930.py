# BOJ - 1793
while True:
    n = int(input())
    if n < 0: break
    a, b = 1, 3
    for _ in range(n-2):
        a, b = b, a*2 + b
    if n < 2:
        print(1)
    else:
        print(b)