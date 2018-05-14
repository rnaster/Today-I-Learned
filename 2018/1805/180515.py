# BOJ - 1660
def BOJ1660():
    n = int(input())
    i = 1
    arr = []
    while True:
        if i*(i+1)*(i+2) // 6 <= n:
            arr.append(i*(i+1)*(i+2) // 6)
            i += 1
        else:
            break
    cache = set(arr)
    ans = 1
    def main():
        global ans, cache
        if n in cache: print(ans); return
        while True:
            temp = set()
            for num in arr:
                for c in cache:
                    if num + c <= n:
                        temp.add(num + c)
                if n in temp: print(ans+1); return
            ans += 1
            cache = temp
    main()

# BOJ - 1699
n = int(input())
arr = []
cache = set()
i = 1
while i*i <= n:
    arr.append(i)
    cache.add(i*i)
    i += 1
ans = 1
def main():
    global cache, ans
    if n in cache: print(ans); return
    while True:
        temp = set()
        for a in arr:
            for c in cache:
                if a*a + c <= n:
                    temp.add(a * a + c)
            if n in temp: print(ans + 1); return
        ans += 1
        cache = temp
main()