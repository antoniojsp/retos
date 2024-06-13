import numpy as np

cost_matrix = np.array([
    [3, 2, 7, 6],
    [7, 5, 2, 3],
    [2, 5, 4, 5]
])

supply = np.array([50, 60, 25])
demand = np.array([60, 40, 20, 15])


def get_minimum_cost_index(cost_matrix):
    min_value = np.min(cost_matrix, axis=0)
    index = np.argwhere(cost_matrix == min_value)
    return min_value, index


def allocate_values(demand, pos, zeros):
    allocation_matrix = zeros.copy()
    for idx, (i, j) in enumerate(pos):
        allocation_matrix[i, j] = demand[j]
    return allocation_matrix


def get_sdiff(cost_matrix, allocated_matrix, supply):
    row_sums = np.sum(allocated_matrix, axis=1)

    sdiff = row_sums - supply
    exceeds_supply = sdiff > 0
    # TODO: Jika masih ada excedds_supply maka
    '''
    1. Cari nilai terkecil berikutnya dengan get_minimum_cost_index, tetapi untuk baris pada index excess row diabaikan
    2. Jika nilai terkecil berikutnya sudah didapatkan, maka alokasikan jumlah supply agar memenuhi baris tersebut
    '''
    return sdiff, exceeds_supply


flc, pos = get_minimum_cost_index(cost_matrix)

zeros = np.zeros_like(cost_matrix)
allocated_matrix = allocate_values(demand, pos, zeros)
print(get_sdiff(cost_matrix, allocated_matrix, supply))