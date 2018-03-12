# BOJ - 13458
n = int(input())
A = tuple(map(int, input().split()))
B, C = map(int, input().split())
A = tuple(map(lambda x: x - B, A))
ans = n
A = tuple(filter(lambda x: x > 0, A))
A = tuple(map(lambda x: x // C if x % C == 0 else x // C + 1, A))
print(ans + sum(A))

quit()
n = int(input())
A = tuple(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for a in A:
    if a <= B:
        ans += 1
    else:
        a = a - B
        ans += 1
        if a <= C:
            ans += 1
        else:
            ans += (a // C + 1) if a % C != 0 else a // C
print(ans)
'''
3
3 4 5
2 2
'''