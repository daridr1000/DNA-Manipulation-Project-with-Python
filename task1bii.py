from linked_list import LinkedList


def string_to_linkedlist(string):
    linked_list = LinkedList()
    previous_node = None
    for i in string:
        previous_node = linked_list.add_after_node(previous_node,i)
    return linked_list


def calculate_hash_values(substring, string_head,x):
    p = t = k = 0
    substring_head = substring.get_head()
    while substring_head is not None and string_head is not None:
        element_1 = string_head._element
        element_2 = substring_head._element
        t +=  (4**(x-(k+1))*get_ord(element_1))
        p +=  (4**(x-(k+1))*get_ord(element_2))
        string_head = string_head._next
        substring_head = substring_head._next
        k+=1
    t%=101
    p%=101
    return t, p


def find_match(string, head_string, substring):
    head_substring = substring.get_head()
    node = head_string
    while head_substring is not None and head_string is not None:
        if head_substring._element != head_string._element:
            return None
        head_string = head_string._next
        head_substring = head_substring._next
    if head_string is None and head_substring is not None:
        return None
    return node


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


def get_k_node(head, k):
    for i in range(k):
        head = head._next
        if head is None:
            return None
    return head

def get_ord(char):
    alph = 'ACGT'
    return 1+alph.index(char)
import sys

line = sys.stdin.readline()
line = line.split()
m = int(line[0])
n = int(line[1])
line = sys.stdin.readline()
line = "".join(line[:-1])
dna_strand = string_to_linkedlist(line)
for j in range(n):
    line = line = sys.stdin.readline()
    line = line.split()
    x, y, s1, i, s2 = line
    x = int(x)
    y = int(y)
    i = int(i)
    h = (4 ** (x - 1)) % 101
    s1 = string_to_linkedlist(s1)
    s2 = string_to_linkedlist(s2)
    s2_aux = reset_s2(s2)
    splice_node = dna_strand.get_head()
    t, p = calculate_hash_values(s1, splice_node,x)
    next_node = get_k_node(splice_node, x - 1)
    while splice_node is not None:
        if t == p:
            current_splice_node = splice_node
            current_next_node = next_node
            splice_node = find_match(dna_strand, splice_node, s1)
            if splice_node is not None:
                dna_strand = splice(dna_strand, s2_aux, i, splice_node)
                s2_aux = reset_s2(s2)
                for l in range(y + i):
                    splice_node = splice_node._next
                    if next_node is not None:
                        next_node = next_node._next
                    if splice_node is None:
                        break
                if splice_node is not None:
                    t, p = calculate_hash_values(s1, splice_node, x)
            else:
                splice_node = current_splice_node._next
                if next_node is not None:
                    next_node = current_next_node._next
                if splice_node is not None:
                    if next_node is not None:
                        t = (4 * (t - get_ord(current_splice_node._element) * h) + get_ord(next_node._element)) % 101
        else:
            current_splice_node = splice_node
            splice_node = splice_node._next
            if splice_node is not None:
                if next_node is not None:
                    next_node = next_node._next
                if next_node is not None:
                    t = (4 * (t - get_ord(current_splice_node._element) * h) + get_ord(next_node._element)) % 101
dna_strand.print_list()
