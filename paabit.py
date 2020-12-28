import numpy as np
from paa import PAA


def PAA_bit(T, n, w):
    T_bit = np.empty((len(T) - n, w - 1), dtype='int')
    for i in range(len(T) - n):
        t_paa = PAA(T[i:i + n], w)
        t_bit = []
        for j in range(len(t_paa) - 1):
            t_bit.append(1 if t_paa[j] < t_paa[j + 1] else 0)
        T_bit[i] = t_bit
    return T_bit
