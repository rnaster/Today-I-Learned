# BOJ - 15312
A = input()
B = input()
dic = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J': 2, 'K': 2, 'L': 1,
       'M': 2, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y':  2, 'Z': 1}
l = []
for i in range(len(A)):
    l.extend([dic[A[i]], dic[B[i]]])
for i in range(len(A) * 2, 2, -1):
    ans = []
    for j in range(i-1):
        ans.append((l[j] + l[j+1]) % 10)
    l = ans[:]
    print(l)
print(str(ans[0]) + str(ans[1]))
'''
CJM
HER
'''