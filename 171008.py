# BOJ - 11722
def foo():
    from sys import stdin, stdout
    from array import array
    read = lambda: stdin.readline().rstrip()
    n = int(read())
    tp = tuple(map(int, read().split()))
    dp = array('I', [1 for _ in range(n)])
    ans = 0
    for i in range(n):
        a = 0
        for j in range(i, n):
            if tp[i] > tp[j] and dp[j] < dp[i] + 1:
                dp[j] += 1
        ans = max(ans, dp[i])
    stdout.write(str(ans))

'''
def main():
    n = int(input())
    a = input().split()
    for i in range(n):
        a[i] = int(a[i])
    
    L = []
    for i in range(n):
        if len(L) == 0:
            L.append(a[i])
        elif L[-1] > a[i]:
            L.append(a[i])
        else:
            row = 0
            high = len(L) - 1
            while row < high:
                mid = (row+high) // 2
                if L[mid] > a[i]:
                    row = mid + 1
                else:
                    high = mid
            L[high] = a[i]
    
    print(len(L))

main()
'''
# BOJ - 11060
from sys import stdin, stdout
from array import array
read = lambda: stdin.readline().rstrip()
n = int(read())
tp = tuple(map(int, read().split()))
dp = array('I', [1001 for _ in range(n)])
dp[0] = 0
for i in range(n):
    bd = min(n, i + tp[i] + 1)
    for j in range(i+1, bd):
        dp[j] = min(dp[j], dp[i] + 1)
if n == 1 and tp[0] != 0: stdout.write('1')
else:
    if dp[-1] == 1001 or tp[0] == 0: stdout.write('-1')
    else: stdout.write(str(dp[-1]))