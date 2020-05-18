# programmers - 2020 kakao blind 기둥과 보
n = 5
build_frame = [[1, 0, 0, 1],
               [1, 1, 1, 1],
               [2, 1, 0, 1],
               [2, 2, 1, 1],
               [5, 0, 0, 1],
               [5, 1, 0, 1],
               [4, 2, 1, 1],
               [3, 2, 1, 1]]
def solution(n, build_frame):
    arr = set()
    for a, b, c, d in build_frame:
        if d == 1:
            if c == 0:
                if b == 0 or \
                        (a, b-1, c) in arr or\
                        (a, b, 1-c) in arr or\
                        (a-1, b, 1-c) in arr:
                    arr.add((a, b, c))
            else:
                if (a, b-1, 1-c) in arr or\
                        (a+1, b-1, 1-c) in arr or\
                        ((a-1, b, c) in arr and (a+1, b, c) in arr):
                    arr.add((a, b, c))
        else:
            if c == 0:
                if (a, b+1, c) not in arr and\
                        (a-1, b+1, 1-c) not in arr and\
                        (a, b+1, 1-c) not in arr:
                    arr.remove((a, b, c))
                else:
                    if (a-1, b+1, 1-c) in arr and\
                            (a-1, b, c) not in arr and\
                            ((a-2, b+1, 1-c) not in arr or
                             (a, b+1, 1-c) not in arr):
                        pass
                    elif (a, b+1, 1-c) in arr and\
                            (a+1, b, c) not in arr and\
                            ((a-1, b+1, 1-c) not in arr or
                             (a+1, b+1, 1-c) not in arr):
                        pass
                    elif (a, b+1, c) in arr and\
                            (a-1, b+1, 1-c) not in arr and\
                            (a, b+1, 1-c) not in arr:
                        pass
                    else:
                        arr.remove((a, b, c))
            else:
                if (a, b, 1-c) not in arr and\
                        (a+1, b, 1-c) not in arr and\
                        (a-1, b, c) not in arr and\
                        (a+1, b, c) not in arr:
                    arr.remove((a, b, c))
                else:
                    if (a+1, b, c) in arr and\
                            (a+1, b-1, 1-c) not in arr and\
                            (a+2, b-1, 1-c) not in arr:
                        pass
                    elif (a-1, b, c) in arr and\
                            (a, b-1, 1-c) not in arr and\
                            (a-1, b-1, 1-c) not in arr:
                        pass
                    elif (a, b, 1-c) in arr and\
                            (a-1, b, c) not in arr and\
                            (a, b-1, 1-c) not in arr:
                        pass
                    elif (a+1, b, 1-c) in arr and\
                            (a+1, b, c) not in arr and\
                            (a+1, b-1, 1-c) not in arr:
                        pass
                    else:
                        arr.remove((a, b, c))
    return[[a, b, c] for a, b, c in sorted(arr)]
print(solution(n, build_frame))
