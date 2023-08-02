## Citation
Please consider citing this repositiory [![DOI](https://zenodo.org/badge/651583706.svg)](https://zenodo.org/badge/latestdoi/651583706)
and our paper 

E. A. Reed, G. Ramos, P. Bogdan and S. Pequito, ["A Scalable Distributed Dynamical Systems Approach to Learn the Strongly Connected Components and Diameter of Networks,"](https://ieeexplore.ieee.org/abstract/document/9904000) in IEEE Transactions on Automatic Control, vol. 68, no. 5, pp. 3099-3106, May 2023, doi: 10.1109/TAC.2022.3209446.

## Code dependencies

To get started with this package, you will first need to insurace that you have installed all of the necessary dependencies.
First, install Python 3.8, 3.9, or 3.10. If you do not already have a Python environment configured on your computer, please see the instructions for installing the full scientific Python stack. https://scipy.org/install.html

* install pip. See the documentation https://pip.pypa.io/en/stable/installation/
* install multiprocess. See the documentation https://pypi.org/project/multiprocess/
* install networkx. See the documentation https://networkx.org/documentation/stable/install.html.

Now you are ready to start using the package. 

There are four functions in this package. Each function computes the output in a distributed manner using the multiprocessing package. Each function takes in a connected directed network intialized using the networkx package. The edge list corresponds to a *list* of *tuples* that are pairs of nodes. The nodes may be given as *strings* or *integers*. 

#### Example:

`edges = [(1, 2), (2, 1), (2, 3), (3, 4), (4, 3), (4, 5), (5, 6), (6, 5)]`

`g1 = nx.DiGraph()`

`g1.add_edges_from(edges)`

## Finite Digraph Diameter

The function `finite_digraph_diameter` finds the finite digraph diameter and returns the value as an *integer*. The finite digraph diameter is the size of longest shortest path between any two nodes where such a path exists. 

#### Example:

`diam = finite_digraph_diameter(g1)`

## Strongly Connected Compenents (SCCs)

The function `strongly_connected_component`s finds the lists of nodes that form the strongly connected components in the network.  Strongly connected components are maximal subgraphs such that for every node in the subgraph there exists a path to every other node in the subgraph. 

#### Example:

`sccs = strongly_connected_components(g1)`

## Source SCCs
The function `source_strongly_connected_components` finds the lists of nodes that form the source strongly connected components in the network. Source strongly connected components are strongly connected components that do not have any incoming edges from other strongly connected components.

#### Example:

`source_sccs = source_strongly_connected_components(g1)`

## Target SCCs

The function `target_strongly_connected_components` finds the lists of nodes that form the target strongly connected components in the network. Target strongly connected components are strongly connected components that do not have any outgoing edges from other strongly connected components.

#### Example:

`target_sccs = target_strongly_connected_components(g1)`

This package welcomes contributors to submit bug fixes, typos, test cases, and new functions that find properties of directed networks in a distributed fashion using the networkx and multiprocessing packages.  

