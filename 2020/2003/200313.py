# BOJ - 1027
n = int(input())
arr = [*map(int, input().split())]
l = [0] * n
for i in range(n):
    a = -9876543210
    for j in range(i+1, n):
        b = (arr[j] - arr[i]) / (j - i)
        if a < b:
            l[i] += 1
            l[j] += 1
            a = b
print(max(l))
"""
15
1 5 3 2 6 3 2 6 4 2 5 7 3 1 5
"""
exit()

# BOJ - 1614
a = int(input()); b = int(input())
if 2 <= a <= 4:
    c, d = divmod(b, 2)
    print(8*c + max(8*d - a + d, a - max(d, 1)))
else:
    c, d = b, a-1
    print(8*c + d)
"""
2
3
"""