import time
import random
import matplotlib.pyplot as plt


def splice(strand, s1, index, s2):
    s1_first_index = strand.find(s1)
    if s1_first_index == -1:
        return strand
    while s1_first_index != -1:
        strand = strand[:(s1_first_index + index)] + s2 + strand[(s1_first_index + index):]
        start = s1_first_index + len(s2) + 1
        s1_first_index = strand.find(s1, start, len(strand))
    return strand


def construct_strand(length):
    strand = ""
    alphabet = 'CTAG'
    for i in range(length):
        random_i = random.randint(0, 3)
        strand += alphabet[random_i]
    return strand


def provide_plots(dimension):
    x = y = dimension
    elements = []
    times = []
    data_structure_elements = []
    data_structure_times = []
    for i in range(100):
        m = 100000*(i + 1)
        print("i:" + str(i + 1))
        average_loading_time = 0
        average_time = 0
        for k in range(20):
            print("k:" + str(k))
            loading_dna_strand_start = time.perf_counter()
            dna_strand = construct_strand(m)
            loading_dna_strand_end = time.perf_counter()
            average_loading_time += (loading_dna_strand_end - loading_dna_strand_start)
            randomx = random.randint(0, m - x)
            randomy = randomx + x
            s1 = dna_strand[randomx:randomy]
            s2 = construct_strand(y)
            index = random.randint(0, x - 1)
            start = time.perf_counter()
            dna_strand = splice(dna_strand, s1, index, s2)
            end = time.perf_counter()
            average_time += (end - start)
        data_structure_elements.append(m)
        average_loading_time /= 20
        data_structure_times.append(average_loading_time)
        average_time /= 20
        times.append(average_time)
        elements.append(m)
    plt.xlabel('Strand Length ' + str(x) + ' restriction')
    plt.ylabel('Time Complexity')
    plt.plot(elements, times, label='Strings')
    plt.grid()
    plt.legend()
    plt.show()

    plt.xlabel('Strand Length ' + str(x) + ' restriction')
    plt.ylabel('Time Complexity')
    plt.plot(data_structure_elements, data_structure_times, label='Strings_Data_Structure')
    plt.grid()
    plt.legend()
    plt.show()
