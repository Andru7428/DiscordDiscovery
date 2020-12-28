import numpy as np
from scipy.spatial import distance
from sax import SAX


def HOTSAX(T, n, w, a, num_discords=1):
    ED_counter = 0
    T_sax = SAX(T, n, w, a)
    words, counts = np.unique(T_sax, return_counts=True)

    best_so_far_dist = 0
    best_so_far_loc = None
    l = len(T)

    outer = np.concatenate([np.where(T_sax == words[i])[0]
                            for i in np.argsort(counts)])
    for p in outer:
        nearest_neighbour_dist = np.Inf
        inner = np.concatenate((np.where(T_sax == T_sax[p])[
                               0], np.random.choice(l - n, size=l - n, replace=False)))
        for q in inner:
            if np.abs(p - q) >= n:
                ED_counter += 1
                dist = distance.euclidean(T[p:p + n], T[q:q + n])
                nearest_neighbour_dist = min(dist, nearest_neighbour_dist)
                if nearest_neighbour_dist < best_so_far_dist:
                    break
        if nearest_neighbour_dist > best_so_far_dist:
            best_so_far_dist = nearest_neighbour_dist
            best_so_far_loc = p

    return (best_so_far_dist, best_so_far_loc,  ED_counter)
