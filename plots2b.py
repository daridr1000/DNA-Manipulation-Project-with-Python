import time
import random
import matplotlib.pyplot as plt

def longer_sequence(a,b):
    if len(a) > len(b):
        return a
    return b

def find_longest_common_sequence(a,b,grid):
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
    data_structure_times_1 = []
    average_loading_time = 0
    average_time = 0
    average_loading_time_1 = 0
    for i in range(10):
        l = 1000*(i+1)
        print("i: "+str(i))
        for j in range(1):
            print("j: "+str(j+1))
            loading_dna_strand_start = time.perf_counter()
            a = construct_strand(l)
            b = construct_strand(l)
            loading_dna_strand_end = time.perf_counter()
            grid = [["" for k in range(len(a) + 1)] for l in range(len(b) + 1)]
            loading_dna_strand_end_1 = time.perf_counter()
            average_loading_time += (loading_dna_strand_end - loading_dna_strand_start)
            average_loading_time_1 += (loading_dna_strand_end_1 - loading_dna_strand_start)
            print(average_loading_time)
            start = time.perf_counter()
            lcs = find_longest_common_sequence(a, b,grid)
            end = time.perf_counter()
            average_time+=(end-start)
            print(average_time)
        data_structure_elements.append(l)
        #average_loading_time /= 20
        data_structure_times.append(average_loading_time)
        data_structure_times_1.append(average_loading_time_1)
        #average_time /= 20
        times.append(average_time)
        elements.append(l)
        print(a,b,lcs)
    plt.xlabel('Strand Lengths')
    plt.ylabel('Time Complexity')
    plt.plot(elements, times, label='Dynamic_Programming')
    plt.grid()
    plt.legend()
    plt.show()

    plt.xlabel('Strand Lengths')
    plt.ylabel('Time Complexity')
    plt.plot(data_structure_elements, data_structure_times, label='Recursive_Data_Structure')
    plt.grid()
    plt.legend()
    plt.show()

    plt.xlabel('Strand Lengths')
    plt.ylabel('Time Complexity')
    plt.plot(data_structure_elements, data_structure_times_1, label='Dynamic_Programming_Data_Structure')
    plt.grid()
    plt.legend()
    plt.show()
provide_plots()