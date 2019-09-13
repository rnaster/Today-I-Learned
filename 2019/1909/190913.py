# BOJ - 14890
n, l = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
def func(row):
    lst = [0] * n
    i = 1
    while i < n:
        if abs(row[i-1] - row[i]) > 1:
            return False
        if row[i-1] - row[i] == 1:
            if n - i >= l:
                for j in range(l):
                    if row[i] != row[i+j]:
                        return False
                    lst[i+j] = 1
                i += l
                continue
            else:
                return False
        if row[i] - row[i-1] == 1:
            if l <= i:
                for j in range(l):
                    if row[i-1] != row[i-1-j] or lst[i-1-j] > 0:
                        return False
                    lst[i-1-j] = 1
            else:
                return False
        i += 1
    return True
for row in arr:
    ans += func(row)
for i in range(n):
    ans += func([arr[j][i] for j in range(n)])
print(ans)
"""
6 2
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2

3 2
9 9 8
8 8 7
8 8 7

4 1
1 2 3 3
2 3 4 5
3 4 5 6
4 5 6 7

7 2
3 3 3 4 4 3 3
2 3 4 4 4 3 2
3 4 4 4 3 2 2
4 5 4 3 3 3 4
5 5 4 3 3 4 5
4 4 4 3 4 4 4
3 4 4 4 4 3 3
"""