from implementations import mat_to_list, reachable


def test_matrix_to_adjacency_list():
    """
    Test conversion from an adjacency matrix to an adjacency list
    """
    adj_mat = [
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    result = mat_to_list(adj_mat)

    assert type(result) is list
    assert len(adj_mat) == len(result)
    assert result == [[1, 3], [2], [0], [4], [3], []]


def test_reachable():
    """
    Test the nodes reachable given an adjacency list
    """
    adj_list1 = [[1, 3], [2], [0], [4], [3], []]
    node1 = 0

    adj_list2 = [[1, 3], [2], [0], [4], [3], []]
    node2 = 3

    result1 = reachable(adj_list1, node1)
    result2 = reachable(adj_list2, node2)

    assert type(result1) is set
    assert result1 == {0, 1, 2, 3, 4}

    assert type(result2) is set
    assert result2 == {3, 4}
