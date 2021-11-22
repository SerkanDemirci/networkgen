from .network import AdjacencyList
from .numba.erdos_renyi import numba_erdos_renyi as _numba_erdos_renyi


def erdos_renyi(num_nodes, edge_prob):
    edge_list = _numba_erdos_renyi(num_nodes, edge_prob)
    return AdjacencyList(edge_list, num_nodes)