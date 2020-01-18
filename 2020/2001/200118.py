# BOJ - 10799
s = input()
a, i, ans = 0, 0, 0
while i < len(s):
    if s[i:i+2] == '()':
        i += 2
        ans += a
    elif s[i] == '(':
        a += 1
        i += 1
    else:
        a -= 1
        ans += 1
        i += 1
print(ans)
"""
()(((()())(())()))(())
"""