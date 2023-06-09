from multiprocessing import Process, Manager
import networkx as nx
from process_algorithm_copy import *



def strongly_connected_components(grph):
    '''
    Function that computes the strongly connected
    components of a digraph and the digraph diameter.
    ------------------------------------------------
    Input:  a networkx digraph with n nodes
            numbered from 0 to n-1
    Output: a list of sets [S_1,...,S_n], the set
            S_i is the SCC where node i belongs
    '''

    # Set initial values
    n = grph.number_of_nodes()
    x = [set([i]) for i in range(n)]
    z = [set() for i in range(n)]
    w = [False] * n
    y = [1] * n
    k = [0]*n

    # compute the in-neighbors of each node
    Nv = [list(grph.predecessors(i)) + [i] for i in range(n)]

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
    processes = []

    while len(to_see) > 0:
        processes = []

        for node in to_see:
            
            # we need to give as input the x,y,z,w (non shared memory) to do the computations and store the computations'
            # results on the shared memory x_shared,y_shared,z_shared,w_shared
            p = Process(target=process_func, args=(node, to_see, x, y, z, w, k, Nv, x_shared, y_shared, z_shared, w_shared, k_shared))
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
        
        diam=max(k)-2
        

    return z, diam

def main():
    # Create a directed graph
    edges = [(x-1,y-1) for x,y in [(1, 2), (2, 1), (2, 3), (3, 4), (4, 3), (4, 5), (5, 6), (6, 5)]]
    G1 = nx.DiGraph()
    G1.add_edges_from(edges)

    # Compute strongly connected components
    sccs, diam = strongly_connected_components(G1)

    # Print the results
    print("Strongly Connected Components of G1:")
    print(sccs)
    print("Diameter of G1:", diam)
    
    edges = [(i,j) for i in range(5) for j in range(5) if i != j ]
    G2 = nx.DiGraph()
    G2.add_edges_from(edges)
    
    # Compute strongly connected components
    sccs, diam = strongly_connected_components(G2)

    # Print the results
    print("Strongly Connected Components of G2:")
    print(sccs)
    print("Diameter of G2:", diam)
    
    edges = [(i-1,j-1) for i,j in [(1,2),(1,3),(2,4),(2,5),(2,6),(4,8),(4,9),(3,7)]]
    G3 = nx.DiGraph()
    G3.add_edges_from(edges)
    
    # Compute strongly connected components
    sccs, diam = strongly_connected_components(G3)

    # Print the results
    print("Strongly Connected Components of G3:")
    print(sccs)
    print("Diameter of G3:", diam)

if __name__ == '__main__':
    main()