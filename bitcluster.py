import numpy as np
from paabit import PAA_bit


def BitSeries_dist(a, b):
    return np.not_equal(a, b).mean()


def BitCluster(T, n, w, k_clusters):
    T_bit = PAA_bit(T, n, w)
    tags = np.zeros(len(T_bit), dtype='int')
    clusters = []
    centers = np.random.choice(len(T_bit), k_clusters, replace=False)
    for center in centers:
        clusters.append({'center': center, 'members': [], 'num_members': 1})
    for i in range(len(T_bit)):
        if (i not in centers):
            p = np.argmin([BitSeries_dist(T_bit[i], T_bit[c])
                           for c in centers])
            tags[i] = p
            clusters[p]['members'].append(i)
            clusters[p]['num_members'] += 1
    return clusters, tags
