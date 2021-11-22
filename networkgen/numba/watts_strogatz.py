from typing import List, Tuple
from numba import njit
import numba
import random

from .ring_lattice import ring_lattice

#TODO: JIT
def watts_strogatz(num_nodes : int, neighbors : int, rewire_probability: float) -> List[Tuple[int, int]]:
    ring = ring_lattice(num_nodes, neighbors)
    adj_list = []
    
    i : int = 0
    while i < num_nodes:
        adj_list.append(set())
        i += 1
    
    i : int = 0
    while i < len(ring):
        s = ring[i][0]
        t = ring[i][1]
        adj_list[s].add(t)
        adj_list[t].add(s)
        i += 1
    
    new_adj_list = adj_list.copy()
    i : int = 0
    while i < num_nodes:
        for j in adj_list[i]:
            if i < j:
                if random.random() < rewire_probability:
                    while True:
                        t : int = int(random.random() * num_nodes)
                        if t != i and t not in new_adj_list[i]:
                            break
                    
                    new_adj_list[i].remove(j)
                    new_adj_list[j].remove(i)
                    
                    new_adj_list[i].add(t)
                    new_adj_list[t].add(i)
                 
        i += 1    
    
    edges = []
    i : int = 0
    while i < num_nodes:
        for j in new_adj_list[i]:
            if i < j:
                edges.append((i, j))
        i += 1
    
    return edges

def warmup_watts_strogatz():
    watts_strogatz(10, 4, 0.5) # Warmup