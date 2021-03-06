

from typing import List, Tuple
import numpy as np
import pandas as pd


__all__ = ["AdjacencyList"]

class BaseNetwork:
    """ Base class for network representations
    """
    _num_nodes   : int
    _num_edges   : int
    _is_directed : False
    
    def __init__(self):
        pass
    
    
    @property
    def num_nodes(self):
        return self._num_nodes
    
    @property
    def num_edges(self):
        return self._num_edges
    
    @property
    def is_directed(self):
        return self._is_directed
    
    def avg_degree(self) -> float:
        ratio = self._num_edges / self._num_nodes 
        return ratio if self._is_directed else 2 * ratio
    
    def max_num_edges(self) -> float:
        n = self._num_nodes
        ratio = n * (n - 1)
        return ratio if self._is_directed else ratio * 0.5
     

class AdjacencyList(BaseNetwork):
    nodes: List[set]
        
    def __init__(self, edge_list : List, num_nodes : int, directed=False):
        super().__init__()
        
        self._is_directed = directed
        self._num_nodes = num_nodes
        self._num_edges = 0
        
        self.nodes = []
        for i in range(num_nodes):
            self.nodes.append(set())
            
        for s, t in edge_list:
            self.add_edge(s, t)
            
        
    def add_edge(self, s : int, t : int) -> None:
        if t not in self.nodes[s]:
            self.nodes[s].add(t)
            self._num_edges += 1
            
            if not self._is_directed:
                self.nodes[t].add(s)
            
    def add_node(self) -> int:
        node_id = self._num_nodes
        self.nodes.append(set())
        self._num_nodes += 1
        
        return node_id
    
    def get_degrees(self) -> np.ndarray:
        degrees = np.zeros(self._num_nodes, dtype=int)
        
        for i, n in enumerate(self.nodes):
            degrees[i] = len(n)
        
        return degrees
    
    def to_edge_list(self) -> np.ndarray:
        edges = np.zeros((self._num_edges, 2), dtype=int)
        
        index = 0
        for s, n in enumerate(self.nodes):
            for t in n:
                if not self._is_directed and s > t:
                    continue
                
                edges[index, 0] = s
                edges[index, 1] = t
                index += 1
        
        return edges
    
    def __str__(self) -> str:
        nodes, edges = self.to_dataframe()
        return f"Nodes:\n{nodes}\nEdges:\n{edges}"
        
    
    def to_dataframe(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        edges = pd.DataFrame(self.to_edge_list(), columns=["Source", "Target"])
        edges["Type"] = "Undirected" 
    
        nodes = pd.DataFrame(range(self._num_nodes), columns=["id"])
        nodes["Degree"] = self.get_degrees()
        
        return nodes, edges
