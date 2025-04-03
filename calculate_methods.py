import numpy as np

def entropy(p):
    p = p[p > 0]
    return -np.sum(p * np.log2(p))

def calculate_information_loss(p_b_a):
    p_a = np.full(p_b_a.shape[0], 1 / p_b_a.shape[0])
    p_b = np.sum(p_b_a * p_a[:, None], axis=0)
    h_b = entropy(p_b)
    h_b_given_a = np.sum([p_a[i] * entropy(p_b_a[i]) for i in range(len(p_a))])
    return h_b - h_b_given_a

def calculate_transfer_time(file_size_kb, channel_capacity_bps):
    file_size_bits = file_size_kb * 8 * 1024
    return file_size_bits / channel_capacity_bps