# BOJ - 7579
from sys import stdin
from pprint import pprint
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
Mem = tuple(map(int, read().split()))
cost = tuple(map(int, read().split()))
dp = [[-1 for _ in range(sum(cost)+1)] for _ in range(n+1)]
# for i in range(n):
#     dp[1][cost[i]] = max(dp[1][cost[i]], Mem[i])
ans = 10001
def main_(i, C):
    global ans, dp
    if i == 1:
        return dp[1][C]
    else:
        val = -1
        for j in range(n):
            if dp[i-1][C-cost[j]] == -1:
                val = max(val, main_(i-1, C-cost[j]))
            else:
                val = max(val, dp[i-1][C-cost[j]])
        dp[i][C] = val
        return val

# main_(n, sum(cost))
# pprint(dp)

def main(i, C):
    global ans, dp
    print(i, C)
    pprint(dp)
    print()
    if i == 0:
        dp[i][C] = 0
        # print(0, i, C, '*', '\n')
        return 0
    # if C == 0:
    #     dp[i][C] = main(i-1, C)
    #     return dp[i][C]
    else:
        if C >= cost[i-1]:
            if dp[i-1][C] != -1 and dp[i-1][C-cost[i-1]] == -1:
                val = max(dp[i-1][C], main(i - 1, C - cost[i - 1]) + Mem[i - 1])
            elif dp[i-1][C] == -1 and dp[i-1][C-cost[i-1]] != -1:
                val = max(main(i - 1, C), dp[i-1][C-cost[i-1]] + Mem[i - 1])
            elif dp[i-1][C] == -1 and dp[i-1][C-cost[i-1]] == -1:
                val = max(main(i - 1, C), main(i - 1, C - cost[i - 1]) + Mem[i - 1])
            else:
                val = max(dp[i-1][C], dp[i-1][C-cost[i-1]] + Mem[i - 1])
            dp[i][C] = max(val, dp[i][C])
            if dp[i][C] >= m: ans = min(ans, C)
            return dp[i][C]
        else:
            if dp[i-1][C] == -1:
                val = main(i-1, C)
            else:
                val = dp[i-1][C]
            dp[i][C] = max(dp[i][C], val)
            if dp[i][C] >= m: ans = min(ans, C)
            return dp[i][C]
main(n, sum(cost))
print()
pprint(dp)
print(ans)

'''
4 10
5 4 6 3 # weight
10 40 30 50 # value

5 60
30 10 20 35 40
3 0 3 5 4

3 9
30 10 20
3 0 3
'''