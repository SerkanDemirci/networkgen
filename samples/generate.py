import networkgen.models as models
import os


PROJECT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)
EXAMPLES_DIR = os.path.join(PROJECT_DIR, "examples")
print("Saving to:", EXAMPLES_DIR)

def generate_network(fun, name, *args, **kwargs):
    network = fun(*args, **kwargs)
    n, e = network.to_dataframe()
    n.to_csv(os.path.join(EXAMPLES_DIR, f"{name}_nodes.csv"), index=False)
    e.to_csv(os.path.join(EXAMPLES_DIR, f"{name}_edges.csv"), index=False)

generate_network(models.erdos_renyi, "erdos_renyi", 100, 0.5)
generate_network(models.barabasi_albert, "barabasi_albert", 100, 3)
generate_network(models.ring_lattice, "ring", 100, 6)
generate_network(models.watts_strogatz, "watts_strogatz", 100, 6, 0.5)

