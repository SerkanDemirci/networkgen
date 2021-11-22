from typing import List, Tuple
from numba import njit
import random

@njit
def numba_barabasi_albert(num_nodes : int, initial_num_nodes : int) -> List[Tuple[int, int]]:
    degrees = []
    edges = []
    
    # Create initial complete graph
    i : int = 0
    total_degrees = 0
    while i < initial_num_nodes:
        j : int = 0
        degrees.append(0)
        while j < i:
            edges.append((i, j))
            degrees[i] += 1
            degrees[j] += 1
            total_degrees += 2
            
            j += 1
            
        i += 1
        
    while len(degrees) < num_nodes:
        new_node : int = len(degrees)
        degrees.append(0)
        
        j : int = 0
        while j < len(degrees) - 1:
            if random.random() < (float(degrees[j]) / float(total_degrees)):
                total_degrees += 2
                degrees[j] += 1
                degrees[new_node] += 1
                edges.append((new_node, j))
                
            j += 1

    return edges 


def numba_warmup_barabasi_albert():
    numba_barabasi_albert(20, 5)