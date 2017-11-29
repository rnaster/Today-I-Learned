# Knapsack algo.
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
def Knapsack():
    n, w = map(int, read().split())
    Ws = tuple(map(int, read().split()))
    vals = tuple(map(int, read().split()))
    dp = array('L', [0 for _ in range(w+1)])
    ans = 0
    s = set()
    for i in range(n):
        temp = set()
        for num in s:
            if num + Ws[i] <= w:
                temp.add(num+Ws[i])
        s = temp.copy()
        s.update({Ws[i] + j for j in Ws[:i] if Ws[i] + j <= w})

        dp[Ws[i]] = max(dp[Ws[i]], vals[i])
        for j in s:
            dp[j] = max(dp[j], dp[j-Ws[i]] + vals[i])
            ans = max(dp[j], ans)
    print(dp)
    # print(dp.index(w))
    '''
    6
    4 10
    5 4 6 3
    10 40 30 50 # 90
    3 30
    5 10 20
    50 60 140 # 200
    3 50
    10 20 30
    60 100 120 # 220
    5 20
    2 3 4 5 9
    3 4 5 8 10
    30 60
    2 3 4 5 9 2 3 4 5 9 2 3 4 5 9 2 3 4 5 9 2 3 4 5 9 2 3 4 5 9
    3 4 5 8 10 4 6 11 2 20 3 4 5 8 10 4 6 11 2 20 3 4 5 8 10 4 6 11 2 20
    40 80
    2 3 4 5 9 2 3 4 5 9 2 3 4 5 9 2 3 4 5 9 2 3 4 5 9 2 3 4 5 9 2 3 4 5 9 2 3 4 5 9
    3 4 5 8 10 4 6 11 2 20 3 4 5 8 10 4 6 11 2 20 3 4 5 8 10 4 6 11 2 20 3 4 5 8 10 4 6 11 2 20
    '''
def fun(n, t, Ws, val):
    arr = array('L', [Ws[0]])
    dp = array('H', [val[0]])
    ans = 10001
    for i in range(1, n):
        for j in range(len(arr)):
            wei = arr[j] + Ws[i]
            if t < wei: continue
            if wei > arr[-1]:
                arr.append(wei)
                dp.append(dp[j] + val[i])
            else:
                idx = bi(arr, wei)
                if arr[idx] == wei:
                    dp[idx] = min(dp[idx], dp[j] + val[i])
                else:
                    arr.insert(idx, wei)
                    dp.insert(idx, dp[j] + val[i])
        if arr[-1] < Ws[i]:
            arr.append(Ws[i])
            dp.append(val[i])
        else:
            idx = bi(arr, Ws[i])
            if arr[idx] == Ws[i]:
                dp[idx] = min(dp[idx], val[i])
            else:
                arr.insert(idx, Ws[i])
                dp.insert(idx, val[i])
        ans = min(ans, dp[-1]) if arr[-1] == t else ans
    print(ans)
    print(arr)
    print(dp)

# BOJ - 7579
n, t = map(int, read().split())
Mem = tuple(map(int, read().split()))
cost = tuple(map(int, read().split()))
dp1 = tuple([0 for _ in range(t+1)])
ans = 10001
for i in range(n):
    dp2 = array('L', [0 for _ in range(t+1)])
    for j in range(t+1):
        if j >= cost[i]:
            dp2[j] = max(dp1[j], dp1[j-cost[i]] + Mem[i])
        else:
            dp2[j] = dp1[j]
        if dp2[j] >= t: ans = min(ans, j)
    dp1 = tuple(dp2[:])
print(ans)


'''
5 10
1 2 3 4 5
5 0 3 2 1
'''
