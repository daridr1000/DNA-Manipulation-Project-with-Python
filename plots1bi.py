from linked_list import LinkedList
import time
import random
import matplotlib.pyplot as plt


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
        current_strand_head = substrand_head
        substrand_head = substrand_head._next
    while substrand_head is not None:
        current_strand_head._next = substrand_head
        current_strand_head = current_strand_head._next
        substrand_head = substrand_head._next
    current_strand_head._next = splice_node
    return strand

def reset_s2(s2,y):
    s2_aux = LinkedList()
    s2_head = s2.get_head()
    previous_node = None
    for l in range(y):
        previous_node = s2_aux.add_after_node(previous_node,s2_head._element)
        s2_head = s2_head._next
    return s2_aux
def construct_linked_list(length):
    strand = LinkedList()
    alphabet = 'CTAG'
    previous_node = None
    for i in range(length):
        random_i = random.randint(0, 3)
        previous_node = strand.add_after_node(previous_node,alphabet[random_i])
    return strand
def string_to_linkedlist(string):
    linked_list = LinkedList()
    previous_node = None
    for i in string:
        previous_node = linked_list.add_after_node(previous_node,i)
    return linked_list
def linked_list_to_string(linked_list):
    string = ""
    head = linked_list.get_head()
    while head is not None:
        string+=head._element
        head = head._next
    return string
def provide_plots(dimension):
    x = y = dimension
    elements = []
    times = []
    data_structure_elements = []
    data_structure_times = []
    for i in range(100):
        m = 10000000*(i+1)
        print("i: " + str(i + 1))
        average_time = 0
        average_loading_time = 0
        for counter in range(20):
            print("counter: " + str(counter))
            loading_dna_strand_start = time.perf_counter()
            dna_strand = construct_linked_list(m)
            loading_dna_strand_end = time.perf_counter()
            dna_strand_string = linked_list_to_string(dna_strand)
            average_loading_time+=(loading_dna_strand_end-loading_dna_strand_start)
            randomx = random.randint(0,m-x)
            randomy = randomx+x
            s1 = string_to_linkedlist(dna_strand_string[randomx:randomy])
            s2 = construct_linked_list(y)
            index = random.randint(0,x-1)
            s2_aux = reset_s2(s2,y)
            splice_node = dna_strand.get_head()
            start = time.perf_counter()
            while splice_node is not None:
                splice_node = find_match(dna_strand, splice_node, s1)
                if splice_node is not None:
                    dna_strand = splice(dna_strand, s2_aux, index, splice_node)
                    s2_aux = reset_s2(s2,y)
                    for l in range(y + index):
                        splice_node = splice_node._next
                        if splice_node is None:
                            break
            end = time.perf_counter()
            average_time+=(end-start)
        data_structure_elements.append(m)
        data_structure_times.append(average_loading_time/20)
        times.append(average_time/20)
        elements.append(m)
    plt.xlabel('Strand Length ' +str(x)+' restriction')
    plt.ylabel('Time Complexity')
    plt.plot(elements, times, label ='Linked_Lists')
    plt.grid()
    plt.legend()
    plt.show()

    plt.xlabel('Strand Length ' +str(x)+' restriction')
    plt.ylabel('Time Complexity')
    plt.plot(data_structure_elements, data_structure_times, label ='Linked_Lists_Data_Structure')
    plt.grid()
    plt.legend()
    plt.show()
