# BOJ - 2011
from sys import stdin
read = lambda: stdin.readline().rstrip()
N = read()
if N[0] == '0': print(0); quit()
if len(N) == 1: print(1); quit()
dp1 = 1
if N[:2] in ['10', '20']: dp2 = 1
elif '11' <= N[:2] <= '26': dp2 = 2
else: dp2 = 1
for i in range(2, len(N)):
    temp = 0
    if N[i] != '0': temp += dp2
    if '10' <= N[i-1:i+1] <= '26': temp += dp1
    dp1, dp2 = dp2, temp % 1000000
print(dp2)
# print(main('17'))

# with open('input.txt', 'r') as f:
#     input = f.readlines()
# with open('output.txt', 'r') as f:
#     output = list(map(int, f.readlines()))
#
# for i in range(len(input)-1):
#     if main(input[i]) != (output[i] % 1000000):
#         print(input[i].rstrip(), '\t', i, main(input[i]), '*')
#         quit()
# print('clear')