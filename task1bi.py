from linked_list import LinkedList

def string_to_linkedlist(string):
    linked_list = LinkedList()
    previous_node = None
    for i in string:
        previous_node = linked_list.add_after_node(previous_node,i)
    return linked_list

def find_match(string,head_string,substring):
    head_substring = substring.get_head()
    while head_string is not None:
        current_head_string = head_string
        current_head_substring = head_substring
        while head_substring._element == head_string._element:
            head_substring = head_substring._next
            head_string = head_string._next
            if head_string is None:
                break
            if head_substring is None:
                break
        if head_substring is None:
            return current_head_string
        head_string = current_head_string._next
        head_substring = current_head_substring
    return None

def splice(strand,substrand,index,splice_node):
    if index != 0:
        for i in range(index):
            current_strand_head = splice_node
            if splice_node is not None:
                splice_node = splice_node._next
    else:
        head = strand.get_head()
        while head._next is not None:
            if head._next == splice_node:
                current_strand_head = head
                break
            head = head._next
        if head._next == None:
            current_strand_head = None
    substrand_head = substrand.get_head()
    if current_strand_head == None:
        strand.add_first(substrand_head._element)
        current_strand_head = strand.get_head()
        substrand_head = substrand_head._next
    while substrand_head is not None:
        current_strand_head._next = substrand_head
        current_strand_head = current_strand_head._next
        substrand_head = substrand_head._next
    current_strand_head._next = splice_node
    return strand

def reset_s2(s2):
    s2_aux = LinkedList()
    s2_head = s2.get_head()
    previous_node = None
    for l in range(y):
        previous_node = s2_aux.add_after_node(previous_node,s2_head._element)
        s2_head = s2_head._next
    return s2_aux

import sys
line=sys.stdin.readline()
line = line.split()
m = int(line[0])
n = int(line[1])
line = sys.stdin.readline()
line = "".join(line[:-1])
dna_strand = string_to_linkedlist(line)
for j in range(n):
    line = line=sys.stdin.readline()
    line = line.split()
    x,y,s1,i,s2 = line
    x = int(x)
    y = int(y)
    i = int(i)
    s1 = string_to_linkedlist(s1)
    s2 = string_to_linkedlist(s2)
    s2_aux = reset_s2(s2)
    splice_node = dna_strand.get_head()
    while splice_node is not None:
        splice_node = find_match(dna_strand,splice_node,s1)
        if splice_node is not None:
            dna_strand = splice(dna_strand,s2_aux,i,splice_node)
            s2_aux = reset_s2(s2)
            for l in range(y+i):
                splice_node = splice_node._next
                if splice_node is None:
                    break
dna_strand.print_list()