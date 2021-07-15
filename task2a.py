def longer_sequence(a,b):
    if len(a) > len(b):
        return a
    return b

def find_longest_common_sequence(a, b, sequence):
    if len(a) == 0 or len(b) == 0:
        return sequence
    if a[-1] == b[-1]:
        sequence = find_longest_common_sequence(a[:-1],b[:-1], a[-1]+sequence)
    sequence = longer_sequence(sequence, longer_sequence(find_longest_common_sequence(a, b[:-1], ""),
                           find_longest_common_sequence(a[:-1], b, "")))
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
    print(find_longest_common_sequence(a,b,""))
