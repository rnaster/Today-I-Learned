# BOJ - 4949
import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s == '.': break
    stack = []
    for ss in s:
        if ss in ['[', '(']:
            stack.append(ss)
        elif ss == ']':
            if len(stack) < 1: stack.append(ss);break
            if stack[-1] == '[':
                stack.pop()
            else:
                break
        elif ss == ')':
            if len(stack) < 1: stack.append(ss);break
            if stack[-1] == '(':
                stack.pop()
            else:
                break
    if len(stack) < 1:
        print('yes')
    else:
        print('no')
"""
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
([)]
.
"""
exit()

# BOJ - 1929
n, m = map(int, input().split())
prime = []
number = list(range(1_000_001))
number[0], number[1] = 0, 0
for i in range(2, 1_000_001):
    if number[i] < 1: continue
    for j in range(2*i, 1_000_001, i):
        number[j] = 0
for i in range(n, m+1):
    if number[i] > 0: print(number[i])
"""
3 16
"""