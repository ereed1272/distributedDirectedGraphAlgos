from multiprocessing import Process, Manager
import networkx as nx
from process     import *


def finite_digraph_diameter(input_graph):
    """
    Function that computes the finite diameter of a directed graph.
    ------------------------------------------------
    Input:  a connected networkx directed graph
    Output: integer value of the finite digraph diameter
    """

    node_relabel = {v: i for i, v in enumerate(list(input_graph.nodes()))}

    grph = nx.DiGraph([(node_relabel[u], node_relabel[v]) for (u, v) in input_graph.edges()])

    # Set initial values
    n = grph.number_of_nodes()
    x = [{i} for i in range(n)]
    z = [set() for i in range(n)]
    w = [False] * n
    y = [1] * n
    k = [0] * n

    # compute the in-neighbors of each node
    nv = [list(grph.predecessors(i)) + [i] for i in range(n)]

    # Create a shared manager for inter-process communication
    manager = Manager()

    # Create shared variables
    x_shared = manager.list(x)
    z_shared = manager.list(z)
    w_shared = manager.list(w)
    y_shared = manager.list(y)
    k_shared = manager.list(k)
    # Create a function for each process
    # Main loop
    to_see = list(range(n))

    while len(to_see) > 0:
        processes = []

        for node in to_see:
            p = Process(target=process_func,
                        args=(node, to_see, x, y, z, w, k, nv[node], x_shared, y_shared, z_shared, w_shared, k_shared))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()
        to_see = [node for node in to_see if not w_shared[node]]

        # Convert shared variables back to normal lists
        k = list(k_shared)
        x = list(x_shared)
        z = list(z_shared)
        w = list(w_shared)
        y = list(y_shared)
    return max(k) - 2


def strongly_connected_components(input_graph):
    '''
    Function that computes the strongly connected
    components of a directed graph.
    ------------------------------------------------
    Input:  a connected networkx directed graph 
    Output: a list of lists containing the nodes that 
    form each of the strongly connected components 
    in the directed graph
    '''

    node_relabel = {v: i for i, v in enumerate(list(input_graph.nodes()))}
    node_relabel_back = {i: v for (v, i) in node_relabel.items()}

    grph = nx.DiGraph([(node_relabel[u], node_relabel[v]) for (u, v) in input_graph.edges()])

    # Set initial values
    n = grph.number_of_nodes()
    x = [{i} for i in range(n)]
    z = [set() for i in range(n)]
    w = [False] * n
    y = [1] * n

    # compute the in-neighbors of each node
    nv = [list(grph.predecessors(i)) + [i] for i in range(n)]

    # Create a shared manager for inter-process communication
    manager = Manager()

    # Create shared variables
    x_shared = manager.list(x)
    z_shared = manager.list(z)
    w_shared = manager.list(w)
    y_shared = manager.list(y)

    # Main loop
    to_see = list(range(n))

    while len(to_see) > 0:
        processes = []

        for node in to_see:
            # we need to give as input the x,y,z,w (non shared memory) to do the computations and store the computations'
            # results on the shared memory x_shared,y_shared,z_shared,w_shared
            p = Process(target=process_func,
                        args=(node, to_see, x, y, z, w, None, nv[node], x_shared, y_shared, z_shared, w_shared, None))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()
        to_see = [node for node in to_see if not w_shared[node]]

        # Convert shared variables back to normal lists
        x = list(x_shared)
        z = list(z_shared)
        w = list(w_shared)
        y = list(y_shared)

    return list(map(list, set(map(tuple, [[node_relabel_back[u] for u in el] for el in z]))))


def source_strongly_connected_components(input_graph):
    '''
    Function that computes the sources strongly connected
    components of a directed graph.
    ------------------------------------------------
    Input:  a networkx directed graph 
    Output: a list of lists containing the nodes 
    that form each of the source strongly connected components 
    in the directed graph
    '''

    node_relabel = {v: i for i, v in enumerate(list(input_graph.nodes()))}
    node_relabel_back = {i: v for (v, i) in node_relabel.items()}

    grph = nx.DiGraph([(node_relabel[u], node_relabel[v]) for (u, v) in input_graph.edges()])

    # Set initial values
    n = grph.number_of_nodes()
    x = [{i} for i in range(n)]
    z = [set() for i in range(n)]
    w = [False] * n
    y = [1] * n
    flag = [(False, False)] * n

    # compute the in-neighbors of each node
    nv = [list(grph.predecessors(i)) + [i] for i in range(n)]

    # Create a shared manager for inter-process communication
    manager = Manager()

    # Create shared variables
    x_shared = manager.list(x)
    z_shared = manager.list(z)
    w_shared = manager.list(w)
    y_shared = manager.list(y)
    flag_shared = manager.list(flag)

    # Main loop
    to_see = list(range(n))

    while len(to_see) > 0:
        processes = []

        for node in to_see:
            # we need to give as input the x,y,z,w (non-shared memory) to do the computations and store the
            # computations'
            # results on the shared memory x_shared,y_shared,z_shared,w_shared
            p = Process(target=process_func, args=(node, to_see, x, y, z, w, None, nv[node], x_shared, y_shared,
                                                   z_shared, w_shared, None, flag, flag_shared, 1))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()
        to_see = [node for node in to_see if not w_shared[node]]

        # Convert shared variables back to normal lists
        x = list(x_shared)
        z = list(z_shared)
        w = list(w_shared)
        y = list(y_shared)
        flag = list(flag_shared)

    return list(map(list, set(map(tuple, [[(node_relabel_back[u]) for u in el] for i, el in enumerate(z)
                                          if flag[i][1]]))))


def target_strongly_connected_components(input_graph):
    '''
    Function that computes the target strongly connected
    components of a directed graph.
    ------------------------------------------------
    Input:  a networkx directed graph 
    Output: a list of lists containing the nodes 
    that form each of the target strongly connected components
    in the directed graph
    '''

    node_relabel = {v: i for i, v in enumerate(list(input_graph.nodes()))}
    node_relabel_back = {i: v for (v, i) in node_relabel.items()}

    grph = nx.DiGraph([(node_relabel[u], node_relabel[v]) for (u, v) in input_graph.edges()])

    # Set initial values
    n = grph.number_of_nodes()
    x = [{i} for i in range(n)]
    z = [set() for i in range(n)]
    w = [False] * n
    y = [1] * n
    flag = [(False, False)] * n

    # compute the in-neighbors of each node
    nv = [list(grph.predecessors(i)) + [i] for i in range(n)]
    nvout = [list(grph.successors(i)) + [i] for i in range(n)]

    # Create a shared manager for inter-process communication
    manager = Manager()

    # Create shared variables
    x_shared = manager.list(x)
    z_shared = manager.list(z)
    w_shared = manager.list(w)
    y_shared = manager.list(y)
    flag_shared = manager.list(flag)

    # Main loop
    to_see = list(range(n))

    while len(to_see) > 0:
        processes = []

        for node in to_see:
            # we need to give as input the x,y,z,w (non shared memory) to do the computations and store the
            # computations'
            # results on the shared memory x_shared,y_shared,z_shared,w_shared
            p = Process(target=process_func, args=(node, to_see, x, y, z, w, None, nv[node], x_shared, y_shared,
                                                   z_shared, w_shared, None, flag, flag_shared, 2, nvout[node]))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()
        to_see = [node for node in to_see if not w_shared[node]]

        # Convert shared variables back to normal lists
        x = list(x_shared)
        z = list(z_shared)
        w = list(w_shared)
        y = list(y_shared)
        flag = list(flag_shared)

    return list(
        map(list, set(map(tuple, [[node_relabel_back[u] for u in el] for i, el in enumerate(z) if flag[i][1]]))))


def main():
    edges = [(x, y) for x, y in [(1, 2), (2, 1), (2, 3), (3, 4), (4, 3), (4, 5), (5, 6), (6, 5)]]
    # names = {1:'mary', 2:'joseph',3:'will',4:'sarah',5:'tom',6:'alex'}
    # edges = [(names[i],names[j]) for i,j, in [(1, 2), (2, 1), (2, 3), (3, 4), (4, 3), (4, 5), (5, 6), (6, 5)]]
    g1 = nx.DiGraph()
    g1.add_edges_from(edges)

    sccs = strongly_connected_components(g1)
    diam = finite_digraph_diameter(g1)
    source = source_strongly_connected_components(g1)
    target = target_strongly_connected_components(g1)

    print("Strongly Connected Components of g1:")
    print(sccs)
    print("Diameter of g1:", diam)
    print("Source:", source)
    print("Target:", target)

    edges = [(i, j) for i in range(5) for j in range(5) if i != j]
    g2 = nx.DiGraph()
    g2.add_edges_from(edges)

    sccs = strongly_connected_components(g2)
    diam = finite_digraph_diameter(g2)
    source = source_strongly_connected_components(g2)
    target = target_strongly_connected_components(g2)

    print("Strongly Connected Components of g2:")
    print(sccs)
    print("Diameter of g2:", diam)
    print("Source:", source)
    print("Target:", target)

    edges = [(i - 1, j - 1) for i, j in [(1, 2), (1, 3), (2, 4), (2, 5), (2, 6), (4, 8), (4, 9), (3, 7)]]
    g3 = nx.DiGraph()
    g3.add_edges_from(edges)

    sccs = strongly_connected_components(g3)
    diam = finite_digraph_diameter(g3)
    source = source_strongly_connected_components(g3)
    target = target_strongly_connected_components(g3)

    print("Strongly Connected Components of g3:")
    print(sccs)
    print("Diameter of g3:", diam)
    print("Source:", source)
    print("Target:", target)

    edges = [[1, 4], [2, 6], [4, 1], [4, 7], [4, 8], [5, 9], [6, 5], [6, 8], [6, 9], [6, 10], [7, 3], [8, 5], [9, 3]]
    g4 = nx.DiGraph()
    g4.add_edges_from(edges)

    # Compute strongly connected components
    sccs = strongly_connected_components(g4)
    diam = finite_digraph_diameter(g4)
    source = source_strongly_connected_components(g4)
    target = target_strongly_connected_components(g4)

    print("Strongly Connected Components of g4:")
    print(sccs)
    print("Diameter of g4:", diam)
    print("Sources: ", source_strongly_connected_components(g4))
    print("Targets: ", target_strongly_connected_components(g4))


if __name__ == '__main__':
    main()
