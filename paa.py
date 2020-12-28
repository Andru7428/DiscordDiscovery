import numpy as np


def PAA(T, w):
    T_paa = np.empty(w)
    cuts_l = int(len(T) / w)
    for i in range(w):
        T_paa[i] = np.mean(T[cuts_l * i:cuts_l * (i + 1)])
    return T_paa
