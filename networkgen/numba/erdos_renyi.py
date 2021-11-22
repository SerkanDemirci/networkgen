from typing import List, Tuple
from numba import njit
import random

@njit
def numba_erdos_renyi(num_nodes : int, edge_prob : float) -> List[Tuple[int, int]]:
    edges = []
    
    i : int = 0
    j : int = 0

    while i < num_nodes:
        j = 0
        while j < i:
            if random.random() < edge_prob:
                edges.append((i, j))
            j += 1
            
        i += 1
    
    return edges

numba_erdos_renyi(5, 0.8) # Warmup