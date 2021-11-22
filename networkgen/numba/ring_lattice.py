from typing import List, Tuple
from numba import njit

@njit
def ring_lattice(num_nodes : int, degree : int) -> List[Tuple[int, int]]:
    edges = []
    
    K : int= degree // 2
    
    i : int = 0

    while i < num_nodes:
        j : int = 1
        while j <= K:
            t = (i + j) % num_nodes
            edges.append((i, t))
            j += 1
        
        '''
        j : int = 1
        while j <= K:
            t = (i - j + num_nodes) % num_nodes
            edges.append((i, t))
            j += 1
        '''
            
        i += 1
    
    return edges

def warmup_ring_lattice():
    ring_lattice(10, 4) # Warmup