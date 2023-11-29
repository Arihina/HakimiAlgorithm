from pprint import pprint

from Dijkstra_algorithm import find_full_path_matrix


def find_line_intersection(line1: tuple[list[int | float], list[int | float | list[int | float]]],
                           line2: tuple[list[int | float], list[int | float | list[int | float]]]) -> \
        (int | float, int | float):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(point1, point2):
        return point1[0] * point2[1] - point1[1] * point2[0]

    div = det(xdiff, ydiff)
    if div == 0:
        # return 0, 0
        raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def get_mark(matrix: list[list[int | float]],
             edges: list[tuple[int, int]]) -> (int, tuple[int, int]):
    marks = [max(min(elem1, elem2) for index, (elem1, elem2) in enumerate(zip(matrix[i], matrix[j]))) for i, j in edges]

    return min(marks), edges[marks.index(min(marks))]


def find_edges(matrix: list[list[int | float]]) -> list[tuple[int, int]]:
    edges = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < j and matrix[i][j] != 0:
                edges.append((i, j))

    return edges


def solve(matrix: list[list[int | float]]) -> None:
    print("Warning! Numbering in edges starts from 0\n")

    edges = find_edges(matrix)
    full_path_matrix = find_full_path_matrix(matrix)
    min_mark, edge = get_mark(full_path_matrix, edges)
    print(f"Min mark = {min_mark} for edge {edge}")

    others_edges = [_ for _ in range(len(full_path_matrix)) if _ not in edge]
    weight = full_path_matrix[edge[0]][edge[1]]

    all_pointers = []
    for i in range(len(others_edges)):
        left_lim_x = 0
        right_lim_x = weight

        point1_y0 = left_lim_x + full_path_matrix[others_edges[i]][edge[0]]
        point1_y1 = right_lim_x + full_path_matrix[others_edges[i]][edge[0]]

        point2_y0 = weight + full_path_matrix[others_edges[i]][edge[1]] - left_lim_x
        point2_y1 = weight + full_path_matrix[others_edges[i]][edge[1]] - right_lim_x

        print(f"d(f, {others_edges[i]}) "
              f"= (x + {full_path_matrix[others_edges[i]][edge[0]]} ; "
              f"{weight + full_path_matrix[others_edges[i]][edge[1]]} - x)")

        point1 = [left_lim_x, point1_y0]
        point2 = [right_lim_x, point1_y1]

        point3 = [left_lim_x, point2_y0]
        point4 = [right_lim_x, point2_y1]

        x_inter, yi_inter = (find_line_intersection((point1, point2), (point3, point4)))
        print(f"Line of intersection: x =  {x_inter}, y = {yi_inter}")

        if yi_inter >= point1_y0:
            all_pointers.append(([left_lim_x, point1_y0], [x_inter, yi_inter]))
        if yi_inter >= point1_y1:
            all_pointers.append(([right_lim_x, point1_y1], [x_inter, yi_inter]))
        if yi_inter >= point2_y0:
            all_pointers.append(([left_lim_x, point2_y0], [x_inter, yi_inter]))
        if yi_inter >= point2_y1:
            all_pointers.append(([right_lim_x, point2_y1], [x_inter, yi_inter]))

    pprint(all_pointers)
