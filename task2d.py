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
strands_matrix = [[]]
for i in range(n):
    line = sys.stdin.readline().split()
    strands_matrix+=[line]
strands_matrix = strands_matrix[1:]
sequences_list = []
for i in range(0,len(strands_matrix)-1):
    for j in range(i+1,len(strands_matrix)):
        sequence = find_longest_common_sequence(strands_matrix[i][0],strands_matrix[j][0])
        sequences_list+=[sequence]
max_common_sequence = ""
for sequence in sequences_list:
    occurences = 0
    for i in range(len(strands_matrix)):
        if sequence in strands_matrix[i][0]:
            occurences+=1
            if occurences == m:
                max_common_sequence = longer_sequence(max_common_sequence,sequence)
                break
print(max_common_sequence)