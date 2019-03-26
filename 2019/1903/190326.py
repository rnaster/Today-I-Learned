# BOJ - 2140
n = int(input())
arr = [input() for _ in range(n)]
if n < 3: print(0);exit()
if n == 3: print(1 if arr[0][0] == '1' else 0);exit()
l = [[-1] * (n-2) for _ in range(n-2)]
l[0][0] = a = 1 if arr[0][0] > '0' else 0
l[1][0] = b = int(arr[1][0]) - l[0][0]
ans = a+b
for i in range(2, n-2):
    l[i][0] = t = int(arr[i][0]) - l[i-1][0] - l[i-2][0]
    ans += t
if l[-1][1] < 0:
    l[-1][1] = c = int(arr[-1][1]) - l[-1][0]
    ans += c
    for i in range(2, n-2):
        l[-1][i] = t = int(arr[-1][i]) - l[-1][i-1] - l[-1][i-2]
        ans += t
if l[0][1] < 0:
    l[0][1] = d = int(arr[0][1]) - l[0][0]
    ans += d
    for i in range(2, n-2):
        l[0][i] = t = int(arr[0][i]) - l[0][i-1] - l[0][i-2]
        ans += t
if l[1][-1] < 0:
    l[1][-1] = e = int(arr[1][-1]) - l[0][-1]
    ans += e
    for i in range(2, n-3):
        l[i][-1] = t = int(arr[i][-1]) - l[i-1][-1] - l[i-2][-1]
        ans += t
print(ans + (n-4)*(n-4))
print(*l, sep='\n')
"""
5
11100
2###1
3###1
2###1
12210

5
11100
2###1
2###2
1###2
01221

4
1221
2##2
2##2
1221
"""
exit()

# BOJ - 1713
n, m = int(input()), int(input())
arr = tuple(map(int, input().split()))
l, a, b = [], 0, 0
vote = [0] * 101
for i in range(m):
    if b < n:
        if arr[i] in l: vote[arr[i]] += 1
        else:
            l.append(arr[i])
            b += 1
            a = 1
            vote[arr[i]] += 1
    else:
        if arr[i] in l:
            vote[arr[i]] += 1
            a = 99999
            for ll in l:
                a = min(a, vote[ll])
        else:
            firstPop = True
            for j in range(n):
                if vote[l[j]] == a:
                    vote[l[j]] = 0
                    l.pop(j)
                    l.append(arr[i])
                    vote[arr[i]] += 1
                    a = 1
                    firstPop = False
                    break
            if firstPop:
                vote[l[0]] = 0
                l.pop(0)
                l.append(arr[i])
                vote[arr[i]] += 1
                a = 1
print(*sorted(l))
"""
3
9
2 1 4 3 5 6 2 7 2
"""