# BOJ - 2469
n = int(input())
k = int(input())
l = [[i for i in range(n)],
     [*map(lambda x: ord(x) - 65, input())]]
i = 1
for i in range(1, k+1):
    s = input()
    if s[0] == "?": break
    for j, ss in enumerate(s):
        if ss == "-":
            l[0][j], l[0][j+1] = l[0][j+1], l[0][j]
arr = [input() for _ in range(k-i)]
for j in range(k-i):
    for b, a in enumerate(arr[-j-1]):
        if a == "-":
            l[1][b], l[1][b+1] = l[1][b+1], l[1][b]
ans = []
for i in range(n-1):
    if l[0][i] == l[1][i]:
        ans.append("*")
    elif l[0][i+1] == l[1][i]:
        l[0][i], l[0][i+1] = l[0][i+1], l[0][i]
        ans.append("-")
    else:
        print("x" * (n - 1))
        exit()

if l[0][-1] == l[1][-1]:
    print("".join(ans))
else:
    print("x" * (n-1))
"""
10
5
ACGBEDJFIH
*-***-***
-*-******
?????????
-**-***-*
**-*-*-*-

10
5
ACGBEDJFIH
*-***-***
-*-******
**-*-***-
-**-***-*
?????????

**-*-*-*-
"""