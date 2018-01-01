from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()

def BOJ2688():
    # BOJ - 2688
    dp = array('L', [1 for _ in range(10)])
    ans = array('L', [0, sum(dp)])
    for _ in range(63):
        dp = array('L', [sum(dp[:i+1]) for i in range(10)])
        ans.append(sum(dp))
    for _ in range(int(read())):
        print(ans[int(read())])

# BOJ - 2618
def f(X, Y):
    return abs(X[0] - Y[0]) + abs(X[1] - Y[1])
dp1, dp2 = (0, 0), (0, 0)
ans = array('B', [])
n = int(read())
w = int(read())
a0, b0 = map(int, read().split())
dp1, dp2 = (dp1[1], f((1, 1), (a0, b0))), (dp2[1], f((n, n), (a0, b0)))
if dp1[1] < dp2[1]: ans.append(1)
else: ans.append(2)
print(dp1, dp2)
if w == 1: print(min(dp1[1], dp2[1])); print(ans[-1]);quit()
a1, b1 = map(int, read().split())
dp1, dp2 = (dp1[1], min(dp1[1] + f((a1, b1), (a0, b0)), dp2[1] + f((1, 1), (a1, b1)))),\
           (dp2[1], min(dp2[1] + f((a1, b1), (a0, b0)), dp1[1] + f((n, n), (a1, b1))))
if dp1[1] < dp2[1]: ans.append(1)
else: ans.append(2)
print(dp1, dp2)
for _ in range(w - 2):
    a, b = map(int, read().split())
    dp1, dp2 = (dp1[1], min(dp1[1] + f((a, b), (a1, b1)), dp2[1] + f((a, b), (a0, b0)))),\
               (dp2[1], min(dp2[1] + f((a, b), (a1, b1)), dp1[1] + f((a, b), (a0, b0))))
    if dp1[1] < dp2[1]: ans.append(1)
    else: ans.append(2)
    a1, b1, a0, b0 = a, b, a1, b1
    print(dp1, dp2)
print(min(dp1[1], dp2[1]))
for i in ans:
    print(i)

'''
6
3
3 5
5 5
2 3
'''
