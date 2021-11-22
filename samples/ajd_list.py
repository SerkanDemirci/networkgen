#!/usr/bin/env python3

from networkgen import AdjacencyList

al = AdjacencyList([[0, 1]], 2)

print(al.num_nodes)
print(al.num_edges)
print(al.avg_degree())
print(al.max_num_edges())
print(al.to_dataframe())