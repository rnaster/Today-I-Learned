# BOJ - 1021
n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(m):
    if arr[i]-1 < n+1-arr[i]:
        t = arr[i]-1
        for j in range(i+1, m):
            arr[j] = (arr[j]-t-1) % n
    else:
        t = n+1-arr[i]
        for j in range(i+1, m):
            arr[j] = (arr[j]+t-1) % n
    ans += t
    n -= 1
print(ans)


"""
10 3
1 2 3

10 3
2 9 5

32 6
27 16 30 11 6 23

10 10
1 6 3 2 7 9 8 4 10 5
"""