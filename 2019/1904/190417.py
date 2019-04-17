# BOJ - 2248
n, l, i = map(int, input().split())
if i == 0: print('0'*n); exit()
def func(a, b, c):
    print(a, b, c)
    if b == 1:
        return '0'*(a-c+1) + '1'*min(1, c-1) + '0'*(c-2)
    if c-1 < 1 << b: return bin(c-1)[2:].zfill(a)
    ans = ''
    p, j = 1, 1
    for j in range(1, a-b+1):
        if c-1 <= (1 << (b+j)) - p:
            ans = '1'.zfill(a-b+1-j)
            break
        p += 1 << j
    p -= 1 << (j-1)
    # print(p, j, (1 << (b+j-1)) - p, '##')
    return ans + func(a-len(ans), b-1, c-((1 << (b+j-1)) - p))
print(func(n, l, i))
"""
5 3 19
"""