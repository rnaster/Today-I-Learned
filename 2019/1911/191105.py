# BOJ - 17609
a = ''
def func(p, q, r):
    for _ in range((q - p + 1) // 2):
        if a[p] == a[q]:
            p += 1
            q -= 1
        elif r:
            r = False
            val = func(p+1, q, r) == 0 or func(p, q-1, r) == 0
            if val:
                return 1
            else:
                return 2
        else:
            return 2
    return 0
for _ in range(int(input())):
    a = input()
    i, j = 0, len(a) - 1
    ans = func(i, j, 1)
    print(ans)

"""
7
abba
summuus
xabba
xabbay
comcom
comwwmoc
comwwtmoc
"""