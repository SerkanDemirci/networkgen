from .network import AdjacencyList
from .numba import erdos_renyi as _erdos_renyi
from .numba import barabasi_albert as _barabasi_albert
from .numba import ring_lattice as _ring_lattice
from .numba import watts_strogatz as _watts_strogatz

warmups = set()

def erdos_renyi(num_nodes : int, edge_prob : float) -> AdjacencyList:
    if "erdos_renyi" not in warmups:
        _erdos_renyi.warmup_erdos_renyi()
        warmups.add("erdos_renyi")
        
    edge_list = _erdos_renyi.erdos_renyi(num_nodes, edge_prob)
    return AdjacencyList(edge_list, num_nodes)


def barabasi_albert(num_nodes : int, initial_num_nodes : int) -> AdjacencyList:
    if "barabasi_albert" not in warmups:
        _barabasi_albert.warmup_barabasi_albert()
        warmups.add("barabasi_albert")
        
    edge_list = _barabasi_albert.barabasi_albert(num_nodes, initial_num_nodes)
    return AdjacencyList(edge_list, num_nodes)

def ring_lattice(num_nodes : int, neighbors : int) -> AdjacencyList:
    if "ring_lattice" not in warmups:
        _ring_lattice.warmup_ring_lattice()
        warmups.add("ring_lattice")
    
    assert neighbors % 2 == 0
    edge_list = _ring_lattice.ring_lattice(num_nodes, neighbors)
    return AdjacencyList(edge_list, num_nodes)

def watts_strogatz(num_nodes : int, neighbors : int, rewire_probability : float) -> AdjacencyList:
    if "watts_strogatz" not in warmups:
        _watts_strogatz.warmup_watts_strogatz()
        warmups.add("watts_strogatz")
    
    assert neighbors % 2 == 0
    edge_list = _watts_strogatz.watts_strogatz(num_nodes, neighbors, rewire_probability)
    return AdjacencyList(edge_list, num_nodes)

