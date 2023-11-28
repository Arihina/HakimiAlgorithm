import math


def get_related_nodes(matrix: list[list[int | float]],
                      node: int):
    for index, weight in enumerate(matrix[node]):
        if weight > 0:
            yield index


def find_min_node(row: list[int | float],
                  visited_nodes: set[int]) -> int:
    min_value = -1
    max_value = max(row)

    for index, elem in enumerate(row):
        if elem < max_value and index not in visited_nodes:
            max_value = elem
            min_value = index

    return min_value


def find_min_path(matrix: list[list[int | float]],
                  node: int) -> list[int | float]:
    length = len(matrix)
    row = [math.inf] * length
    visited_nodes = {node}
    row[node] = 0

    while node != -1:
        for i in get_related_nodes(matrix, node):
            if i not in visited_nodes:
                weight = row[node] + matrix[node][i]
                if weight < row[i]:
                    row[i] = weight
        node = find_min_node(row, visited_nodes)
        if node >= 0:
            visited_nodes.add(node)

    return row


def find_full_path_matrix(matrix: list[list[int | float]]) -> list[list[int | float]]:
    return [find_min_path(matrix, node) for node in range(len(matrix[0]))]
