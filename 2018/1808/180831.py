# BOJ - 1789
n = int(input())
m = 1
while True:
    if m * (m + 1) < n * 2:
        m += 1
    else: print(m-1);exit()