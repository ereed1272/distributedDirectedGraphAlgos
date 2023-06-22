To get started with this package, you will first need to insurace that you have installed all of the necessary dependencies.
First, install Python 3.8, 3.9, or 3.10. If you do not already have a Python environment configured on your computer, please see the instructions for installing the full scientific Python stack. https://scipy.org/install.html

Then, install pip. See the documentation https://pip.pypa.io/en/stable/installation/
Then, install multiprocess. See the documentation https://pypi.org/project/multiprocess/
Then, install networkx. See the documentation https://networkx.org/documentation/stable/install.html.

Now you are ready to start using the package. 

There are four functions in this package. Each function computes the output in a distributed manner using the multiprocessing package. Each function takes in a connected directed network intialized using the networkx package. The edge list may be given as strings or integers. 

Example:

edges = [(1, 2), (2, 1), (2, 3), (3, 4), (4, 3), (4, 5), (5, 6), (6, 5)]
G1 = nx.DiGraph()
G1.add_edges_from(edges)

The function finite_digraph_diameter finds the finite digraph diameter and returns the value as an integer. The finite digraph diameter is the longest shortest path between any two nodes where such a path exists. 
Example:
diam = finite_digraph_diameter(G1)

The function strongly_connected_components finds the lists of nodes that form the strongly connected components in the network.  Strongly connected components are maximal subgraphs in from every node in the subgraph there exists a path to every other node in the subgraph. 

sccs = strongly_connected_components(G1)

The function source_strongly_connected_components finds the lists of nodes that form the source strongly connected components in the network. Source strongly connected components are strongly connected components that do not have any incoming edges from other strongly connected components.

source_sccs = source_strongly_connected_components(G1)

The function target_strongly_connected_components finds the lists of nodes that form the target strongly connected components in the network. Target strongly connected components are strongly connected components that do not have any outgoing edges from other strongly connected components.

target_sccs = target_strongly_connected_components(G1)

This package welcomes contributors to submit bug fixes, typos, test cases, and new functions that find properties of directed networks in a distributed fashion using the networkx and multiprocessing packages.  

