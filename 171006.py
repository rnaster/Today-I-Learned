# BOJ - 9251
from sys import stdin, stdout
from array import array
read = lambda: stdin.readline().rstrip()
char1 = read()
char2 = read()
outer = len(char1)
inner = len(char2) + 1
arr = array('I', [0 for _ in range(inner)])
for row in range(outer):
    temp = array('I', [0 for _ in range(inner)])
    for col in range(1, inner):
        if char1[row] == char2[col-1]:
            if row == 0 or col == 1: temp[col] = 1
            else: temp[col] = max(arr[:col]) + 1
        else:
            pass
        arr[col] = max(arr[col], temp[col])
    print(temp)
    print(arr,'*')
stdout.write(str(max(arr)))