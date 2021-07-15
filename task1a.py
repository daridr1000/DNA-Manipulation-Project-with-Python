
def splice(strand,s1,index,s2):
    s1_first_index = strand.find(s1)
    if s1_first_index == -1:
        return strand
    while s1_first_index != -1:
        strand = strand[:(s1_first_index+index)] + s2 + strand[(s1_first_index+index):]
        start = s1_first_index + len(s2) + 1
        s1_first_index = strand.find(s1,start,len(strand))
    return strand

def solution():
    line=sys.stdin.readline()
    line = line.split()
    m = int(line[0])
    n = int(line[1])
    line = sys.stdin.readline()
    dna_strand = "".join(line[:-1])
    for j in range(n):
        line = line=sys.stdin.readline()
        line = line.split()
        x,y,s1,i,s2 = line
        i = int(i)
        dna_strand = splice(dna_strand,s1,i,s2)
    print(dna_strand)

import sys
solution()