from copy import deepcopy

def compute_scc(node, x, y, z, w, k, Nv):
    # Step 1
    xi = set.union(*[x[j] for j in Nv[node]])

    # Step 2
    yi = len(xi)

    # Step 3
    zi = [j for j in xi if yi == y[j]]

    # Step 4
    w[node] = (yi == y[node] and len(zi) == len(z[node]))
    x[node] = xi
    y[node] = yi
    z[node] = zi
    k[node] +=1

    return x,y,z,w,k

def process_func(node, to_see, x, y, z, w, k, Nv, x_shared, y_shared, z_shared, w_shared, k_shared):
    x,y,z,w,k = compute_scc(node, x, y, z, w, k, Nv)
    w_result = w[node]
    k_shared[node] = k[node]
    x_shared[node] = x[node]
    y_shared[node] = y[node]
    z_shared[node] = z[node]
    w_shared[node] = w[node]
    
    if w_result:
        to_see.append(node)
