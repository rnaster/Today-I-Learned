# BOJ - 5582
from sys import stdin
read = lambda: stdin.readline().rstrip()
char1 = read()
char2 = read()
length1 = len(char1)
length2 = len(char2)
dp = [[0 for _ in range(length2)] for _ in range(length1)]
ans = 0
for i in range(length1):
    for j in range(length2):
        if dp[i][j] == 0 and char1[i] == char2[j]:
            tmp = 0
            for idx in range(min(length1-i, length2-j)):
                if char1[i+idx] == char2[j+idx]:
                    tmp += 1
                    dp[i+idx][j+idx] = 1
                else:
                    dp[i+idx][j+idx] = 1
                    break
            ans = max(tmp, ans)
        if ans >= length2-j: break
    if ans >= length1-i: break
print(ans)