def compute_scc(node, x, y, z, w, k, nv, flag, flag_shared, source_or_target, nv_out):
    # Step 1
    xi = set.union(*[x[j] for j in nv])

    # Step 2
    yi = len(xi)

    # Step 3
    zi = [j for j in xi if yi == y[j]]

    # Step 4
    w[node] = (yi == y[node] and len(zi) == len(z[node]))
    x[node] = xi
    y[node] = yi
    z[node] = zi
    if k is not None:
        k[node] += 1
    if source_or_target == 1:
        tmp = all(el in z[node] for el in nv)
        flag[node] = (tmp, tmp and all([flag_shared[ng][0] for ng in nv]))
    elif source_or_target == 2:
        tmp = all(el in z[node] for el in nv_out)
        flag[node] = (tmp, tmp and all([flag_shared[ng][0] for ng in nv if ng in z[node]]))
    return x, y, z, w, k, flag


def process_func(node, to_see, x, y, z, w, k, nv, x_shared, y_shared, z_shared, w_shared, k_shared, flag=None, flag_shared=None, source_or_target=0, nv_out=None):
    x, y, z, w, k, flag = compute_scc(node, x, y, z, w, k, nv, flag, flag_shared, source_or_target, nv_out)
    w_result = w[node]
    if k is not None:
        k_shared[node] = k[node]
    x_shared[node] = x[node]
    y_shared[node] = y[node]
    z_shared[node] = z[node]
    w_shared[node] = w[node]
    if source_or_target:
        flag_shared[node] = flag[node]
    if w_result:
        to_see.append(node)
