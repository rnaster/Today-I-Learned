from sys import stdin

read = lambda : stdin.readline().rstrip()

def BOJ1764():
    # BOJ - 1764
    n, m = map(int, read().split())
    ans = []
    s = set()
    for _ in range(n):
        s.add(read())
    for _ in range(m):
        string = read()
        if string in s:
            ans.append(string)
    print(len(ans))
    ans.sort()
    for a in ans:
        print(a)
    '''
    3 4
    ohhenrie
    charlie
    baesangwook
    obama
    baesangwook
    ohhenrie
    clinton
    '''
# BOJ - 12790
for _ in range(int(read())):
    H, M, A, D, H_, M_, A_, D_ = map(int, read().split())
    H = H + H_ if H + H_ > 1 else 1
    M = M + M_ if M + M_ > 1 else 1
    A = A + A_ if A + A_ > 0 else 0
    D += D_
    print( H + 5 * M + 2 * A + 2 * D)

'''
3
100 100 100 100 0 0 0 0
10 20 30 40 40 30 20 10
100 100 100 100 -200 0 400 400
'''