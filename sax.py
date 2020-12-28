import numpy as np
from scipy.stats import norm
from paa import PAA
import string


def SAX(T, n, w, a):
    T_sax = np.empty(len(T) - n, dtype=np.dtype('U' + str(w)))
    breakpoints = norm.ppf(np.linspace(0, 1, a + 1)[1:])
    alphabet = string.ascii_lowercase
    for i in range(len(T) - n):
        t_paa = PAA(T[i:i + n], w)
        T_sax[i] = str.join(
            '', [alphabet[np.argmax(t < breakpoints)] for t in t_paa])
    return T_sax
