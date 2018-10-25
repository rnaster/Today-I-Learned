# BOJ - 1788
n = int(input())
if n == 0: print(0);print(0);exit()
elif n % 2 == 1 or n > 0: print(1)
else: print(-1)
a, b = 0, 1
for _ in range(abs(n)):
    a, b = b, (a+b) % 1000000000
print(a)