import numpy as np
from bitcluster import BitCluster
from scipy.spatial import distance


def BitClusterDiscord(T, n, w, k_clusters):
    ED_counter = 0
    T_clusters, tags = BitCluster(T, n, w, k_clusters)

    best_so_far_dist = 0
    best_so_far_loc = None
    l = len(T)

    T_clusters_sorted = sorted(T_clusters, key=lambda i: i['num_members'])
    outer = np.concatenate([c['members'] for c in T_clusters_sorted])
    outer = outer.astype('int')
    for p in outer:
        nearest_neighbour_dist = np.Inf
        inner = np.concatenate((T_clusters[int(tags[p])]['members'], np.random.choice(
            l - n, size=l - n, replace=False)))
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

    return (best_so_far_dist, best_so_far_loc, ED_counter)
