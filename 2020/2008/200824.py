# programmers - 2020 kakao intern
n = 9
path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
order = [[8, 5], [6, 7], [4, 1]]
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[4,1],[8,7],[6,5]]
n = 2
path = [[0, 1]]
order = [[1, 0]]
def solution(n, path, order):
    arr = [[] for _ in range(n)]
    for p in path:
        arr[p[0]].append(p[1])
        arr[p[1]].append(p[0])
    l = [[] for _ in range(n)]
    visit = [[True] * n for _ in range(2)]
    for o in order:
        l[o[0]].append(o[1])
        visit[1][o[1]] = False
    if visit[1][0]: q = [0]
    else: return False
    while q:
        a = q.pop()
        for b in l[a]:
            visit[1][b] = True
            if not visit[0][b]:
                q.append(b)
        for b in arr[a]:
            if visit[0][b]:
                visit[0][b] = False
                if visit[1][b]:
                    q.append(b)
    return all(visit[1])
print(solution(n, path, order))
