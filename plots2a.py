import time
import random
import matplotlib.pyplot as plt

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

def construct_strand(length):
    strand = ""
    alphabet = 'CTAG'
    for i in range(length):
        random_i = random.randint(0, 3)
        strand += alphabet[random_i]
    return strand
def provide_plots():
    elements = []
    times = []
    data_structure_elements = []
    data_structure_times = []
    average_loading_time = 0
    average_time = 0
    for i in range(1):
        l = 13
        print("i: "+str(i))
        for j in range(1):
            print("j: "+str(j+1))
            loading_dna_strand_start = time.perf_counter()
            a = construct_strand(l)
            b = construct_strand(l)
            loading_dna_strand_end = time.perf_counter()
            average_loading_time += (loading_dna_strand_end - loading_dna_strand_start)
            print(average_loading_time)
            start = time.perf_counter()
            lcs = find_longest_common_sequence(a, b, "")
            end = time.perf_counter()
            average_time+=(end-start)
            print(average_time)
        data_structure_elements.append(l)
        #average_loading_time /= 20
        data_structure_times.append(average_loading_time)
        #average_time /= 20
        times.append(average_time)
        elements.append(l)
        print(a,b,lcs)
    plt.xlabel('Strand Lengths')
    plt.ylabel('Time Complexity')
    plt.plot(elements, times, label='Recursive')
    plt.grid()
    plt.legend()
    plt.show()

    plt.xlabel('Strand Lengths')
    plt.ylabel('Time Complexity')
    plt.plot(data_structure_elements, data_structure_times, label='Recursive_Data_Structure')
    plt.grid()
    plt.legend()
    plt.show()
provide_plots()