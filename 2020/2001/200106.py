# BOJ - 17610
n = int(input())
arr = [*map(int, input().split())]
dp = {0}
for a in arr:
    temp = set()
    for b in dp:
        temp.update({max(0, b-a), max(0, a-b), b+a, b})
    dp.update(temp)
print(sum(arr) - len(dp) + 1)
"""
3
1 5 7
"""