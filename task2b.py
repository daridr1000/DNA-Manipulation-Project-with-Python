def longer_sequence(a,b):
    if len(a) > len(b):
        return a
    return b
def find_longest_common_sequence(a,b):
    grid = [["" for k in range(len(a) + 1)] for l in range(len(b) + 1)]
    sequence = ""
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0 or j == 0:
                grid[i][j] = ""
            elif a[i-1] == b[j-1]:
                grid[i][j] = grid[i-1][j-1]+a[i-1]
                sequence = longer_sequence(sequence,grid[i][j])
            else:
                grid[i][j] = ""
    return sequence

import sys
line = sys.stdin.readline()
n,m,l = line.split()
n = int(n)
m = int(m)
l = int(l)
if n == 2 and m == 1:
    a = sys.stdin.readline()
    a = a[:-1]
    b = sys.stdin.readline()
    b = b[:-1]
    print(find_longest_common_sequence(a,b))