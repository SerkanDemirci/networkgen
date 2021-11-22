
# networkgen

A python module to create random networks using network models

## Usage
```bash
$ networkgen <model> <model-args> ...
```

### Network Models
#### Erdős–Rényi
```bash
$ networkgen erdos_renyi <num_nodes> <edge_prob>
```

<img src="examples/erdos_renyi.png?raw=true" width="256"/>

#### Barabási–Albert
```bash
$ networkgen barabasi_albert <num_nodes> <initial_num_nodes>
```

<img src="examples/barabasi_albert.png?raw=true" width="256"/>

#### Watts–Strogatz

```bash
$ networkgen barabasi_albert <num_nodes> <num_neighbors> <rewire_probability>
```

<img src="examples/watts_strogatz.png?raw=true" width="256"/>

#### Ring Lattice

```bash
$ networkgen ring_lattice <num_nodes> <num_neighbors>
```

## TODO: Models
- [x] Erdős–Rényi
- [x] Barabási–Albert
- [x]  Watts–Strogatz
- [x] Ring-Lattice
- [ ] Complete 