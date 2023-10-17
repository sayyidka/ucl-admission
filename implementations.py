def mat_to_list(adj_mat):
    """Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
    adj_list = []
    for vector in adj_mat:
        occurences = [i for i, v in enumerate(vector) if v == 1]
        adj_list.append(occurences)
    return adj_list


def reachable(adj_list, start_node):
    """Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    reachable = {start_node}
    visited_nodes = [start_node]
    visiting = start_node

    while len(visited_nodes) < len(adj_list):
        node_list = adj_list[visiting]
        if node_list:
            visited_nodes.append(visiting)
            [reachable.add(n) for n in adj_list[visiting]]
            for item in node_list:
                visiting = item
                [reachable.add(n) for n in adj_list[visiting]]
                visited_nodes.append(item)
    return reachable
