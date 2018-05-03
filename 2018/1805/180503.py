# BOJ - 2869
a, b, v = map(int, input().split())
def func(a, b, v):
    ans = 0
    while True:
        q = v // a
        v -= q * (a - b)
        ans += q
        if v <= a: ans += 1; return ans
print(func(a, b, v))
'''
2 1 5
'''
