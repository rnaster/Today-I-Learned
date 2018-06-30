# BOJ - 2986
import sys
n = int(input())
i = 2
while i*i <= n:
    if n % i == 0: print(n - n // i); sys.exit()
    i += 1
print(n-1)