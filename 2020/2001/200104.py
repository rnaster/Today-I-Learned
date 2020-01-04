# BOJ - 2812
a, k = map(int, input().split())
c = input()
ans = []
for i in range(a):
    while k > 0:
        if len(ans) > 0 and ans[-1] < c[i]:
            k -= 1
            ans.pop()
        else:
            ans.append(c[i])
            break
    else:
        ans.append(c[i:])
        break
if k > 0:
    print(''.join(ans[:-k]))
else:
    print(''.join(ans))
"""
4 2
1924
"""