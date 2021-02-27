# BOJ - 6884
p = []
l = [True] * 10_000
l[0] = l[1] = False
for i in range(2, 10_000):
    if l[i]:
        p.append(i)
        for j in range(i*i, 10_000, i):
            l[j] = False
def func(a):
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    if a < 10_000:
        return l[a]
    for i in p:
        if i*i <= a and a % i == 0:
            return False
    return True
for _ in range(int(input())):
    arr = map(int, input().split())
    n = next(arr)
    arr = [*arr]
    cache = arr[:]
    flag = True
    for i in range(1, n):
        for j in range(n-i):
            cache[j] += arr[j+i]
            if func(cache[j]):
                flag = False
                print("Shortest primed subsequence is length %s:" % (i+1), end=" ")
                for k in range(i+1):
                    print("%s" % arr[j+k], end=" ")
                break
        if not flag:
            break
    if flag:
        print("This sequence is anti-primed.")
    else:
        print()
"""
3
5 3 5 6 3 8
5 6 4 5 4 12
21 15 17 16 32 28 22 26 30 34 29 31 20 24 18 33 35 25 27 23 19 21

1
5 10000 0 2 1 1
"""
exit()

# BOJ - 2258
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
t, p = 0, 0
for a, b in sorted([[*map(int, read().split())] for _ in range(n)],
                   key=lambda x: (x[1], -x[0])):
    if m > a:
        m -= a
        if p == b:
            t += b
        else:
            t = p = b
    else:
        if p == b:
            if m > 0:
                t += b
                m = 0
        else:
            if m == 0:
                print(min(t, b))
            else:
                print(b)
            exit()
if m == 0:
    print(t)
else:
    print(-1)
"""
4 10000
10000 20
1000 1
2000 2
5000 8

4 3
1 2
3 2
2 2
5 7

4 9
1 5
2 5
10 5
4 6

4 1
1 5
1 5
1 5
1 5
2 6


"""
exit()

# BOJ - 16917
a, b, c, x, y = map(int, input().split())
ans = 0
t = min(x, y)
x -= t
y -= t
if 2*c <= a + b:
    ans += t * 2*c
else:
    ans += t * (a+b)
if x == 0:
    if 2*c <= b:
        ans += y * 2*c
    else:
        ans += y * b
else:
    if 2 * c <= a:
        ans += x * 2*c
    else:
        ans += x * a
print(ans)
"""
1500 2000 1600 3 2

1500 2000 1900 3 2

1500 2000 500 90000 100000
"""
exit()

# BOJ - 2980
n, m = map(int, input().split())
t, ans = 0, 0
for _ in range(n):
    a, b, c = map(int, input().split())
    ans += a - t
    q = ans % (b+c)
    if q < b:
        ans += b - q
    t = a
ans += m - t
print(ans)
"""
2 10
3 5 5
5 2 2
"""