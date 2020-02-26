# BOJ - 2512
from bisect import bisect_left as bi
n = int(input())
arr = sorted(map(int, input().split()))
k = int(input())
if sum(arr) <= k: print(arr[-1]);exit()
i, j = 0, n-1
a, b = 0, arr[j]
ans = (a+b) // 2
idx = bi(arr, ans, i, j)
c = sum(arr[:idx])
while a < ans < b:
    tmp = c + (n-idx) * ans
    if k > tmp:
        a = ans
        ans = (a + b) // 2
        i = idx
        idx = bi(arr, ans, i, j)
        c += sum(arr[i:idx])
    elif k < tmp:
        b = ans
        ans = (a + b) // 2
        j = idx
        idx = bi(arr, ans, i, j)
        c -= sum(arr[idx:j])
    else:
        break
print(ans)
"""
4
120 110 140 150
485

5
4 4 5 5 2
7
"""