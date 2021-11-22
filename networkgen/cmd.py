import argparse
import os
from networkgen.generators import erdos_renyi, barabasi_albert
from networkgen.network import AdjacencyList


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def networkgen_command():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='Network Models')
    
    parser.add_argument("-d", "--dest", type=dir_path, default=".")
    parser.add_argument("-n", "--name", type=str, default="network")

    erdos_renyi_parser = subparsers.add_parser("erdos_renyi")
    erdos_renyi_parser.set_defaults(func=subcommand_erdos_renyi)
    erdos_renyi_parser.add_argument("num_nodes", type=int)
    erdos_renyi_parser.add_argument("edge_probability", type=float)
    
    
    barabasi_albert_parser = subparsers.add_parser("barabasi_albert")
    barabasi_albert_parser.set_defaults(func=subcommand_barabasi_albert)
    barabasi_albert_parser.add_argument("num_nodes", type=int)
    barabasi_albert_parser.add_argument("initial_num_nodes", type=int)

    args = parser.parse_args()
    args.func(parser, args)
    
    
def subcommand_erdos_renyi(parser, args):
    if args.num_nodes <= 0:
        parser.error(f"Num nodes must be a positive integer. Got: {args.num_nodes}")
    
    if args.edge_probability < 0 or args.edge_probability > 1:
        parser.error(f"Edge probability must be a in between [0, 1]. Got: {args.edge_probability}")
    
    network : AdjacencyList = erdos_renyi(args.num_nodes, args.edge_probability)
    
    nodes, edges = network.to_dataframe()
    
    nodes.to_csv(os.path.join(args.dest, f"{args.name}_nodes.csv"), index=False)
    edges.to_csv(os.path.join(args.dest, f"{args.name}_edges.csv"), index=False)
    
def subcommand_erdos_renyi(parser, args):
    if args.num_nodes <= 0:
        parser.error(f"Num nodes must be a positive integer. Got: {args.num_nodes}")
    
    if args.edge_probability < 0 or args.edge_probability > 1:
        parser.error(f"Edge probability must be a in between [0, 1]. Got: {args.edge_probability}")
    
    network : AdjacencyList = erdos_renyi(args.num_nodes, args.edge_probability)
    
    nodes, edges = network.to_dataframe()
    
    nodes.to_csv(os.path.join(args.dest, f"{args.name}_nodes.csv"), index=False)
    edges.to_csv(os.path.join(args.dest, f"{args.name}_edges.csv"), index=False)
    
    
def subcommand_barabasi_albert(parser, args):
    if args.num_nodes <= 0:
        parser.error(f"Num nodes must be a positive integer. Got: {args.num_nodes}")
    
    if args.initial_num_nodes >= args.num_nodes:
        parser.error(f"Initial num nodes must be less than num nodes. Got: {args.initial_num_nodes} > {args.num_nodes}")
    
    network : AdjacencyList = barabasi_albert(args.num_nodes, args.initial_num_nodes)
    
    nodes, edges = network.to_dataframe()
    nodes.to_csv(os.path.join(args.dest, f"{args.name}_nodes.csv"), index=False)
    edges.to_csv(os.path.join(args.dest, f"{args.name}_edges.csv"), index=False)
