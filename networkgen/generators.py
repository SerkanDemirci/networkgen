from .network import AdjacencyList
from .numba import erdos_renyi as _erdos_renyi
from .numba import barabasi_albert as _barabasi_albert

warmups = set()

def erdos_renyi(num_nodes : int, edge_prob : float) -> AdjacencyList:
    if "erdos_renyi" not in warmups:
        _erdos_renyi.numba_warmup_erdos_renyi()
        warmups.add("erdos_renyi")
        
    edge_list = _erdos_renyi.numba_erdos_renyi(num_nodes, edge_prob)
    return AdjacencyList(edge_list, num_nodes)


def barabasi_albert(num_nodes : int, initial_num_nodes : int) -> AdjacencyList:
    if "barabasi_albert" not in warmups:
        _barabasi_albert.numba_warmup_barabasi_albert()
        warmups.add("barabasi_albert")
        
    edge_list = _barabasi_albert.numba_barabasi_albert(num_nodes, initial_num_nodes)
    return AdjacencyList(edge_list, num_nodes)
