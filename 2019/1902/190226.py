# BOJ - 3054
a = input()
b = len(a)
if b < 2:
    print('..#..', '.#.#.', '#.%s.#' %a, '.#.#.', '..#..', sep='\n')
    exit()
print('..', end='')
for i in range(1, b):
    if i % 3: print('#...', end='')
    else: print('*...', end='')
if b % 3: print('#..')
else: print('*..')
print('.', end='')
for i in range(1, b+1):
    if i % 3: print('#.#.', end='')
    else: print('*.*.', end='')
print('')
for i in range(1, b+1):
    if i % 3 == 0 or i >= 2 and (i-1) % 3 == 0: print('*.%s.' % a[i-1], end='')
    else: print('#.%s.' % a[i-1], end='')
if b % 3: print('#')
else: print('*')
print('.', end='')
for i in range(1, b+1):
    if i % 3: print('#.#.', end='')
    else: print('*.*.', end='')
print('')
print('..', end='')
for i in range(1, b):
    if i % 3: print('#...', end='')
    else: print('*...', end='')
if b % 3: print('#..')
else: print('*..')
"""
D
..#..
.#.#.
#.D.#
.#.#.
..#..

DO
..#...#..
.#.#.#.#.
#.D.#.O.#
.#.#.#.#.
..#...#..

DOG
..#...#...*..
.#.#.#.#.*.*.
#.D.#.O.*.G.*
.#.#.#.#.*.*.
..#...#...*..
"""