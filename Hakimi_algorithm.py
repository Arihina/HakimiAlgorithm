from tkinter.messagebox import showinfo

import graph
from Dijkstra_algorithm import find_full_path_matrix
from aliases import TTupleList, TPointsTuple, TMatrix, TEdge


def delete_duplicates(lst: TTupleList) -> list:
    new_lst = []
    for elem in lst:
        if elem not in new_lst:
            if elem not in new_lst:
                point1, point2 = elem[0], elem[1]
                if point1[0] != point2[0] and point1[1] != point2[1]:
                    new_lst.append(elem)

    return new_lst


def find_line_intersection(line1: TPointsTuple, line2: TPointsTuple) -> (int | float, int | float):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(point1, point2):
        return point1[0] * point2[1] - point1[1] * point2[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return 0, 0

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def find_points_on_graph(others_edges: list[int], weight: int | float,
                         full_path_matrix: TMatrix,
                         edge: TEdge) -> (TTupleList, graph.TPyplot):
    all_pointers = []
    for i in range(len(others_edges)):
        left_lim_x = 0
        right_lim_x = weight

        point1_y0 = left_lim_x + full_path_matrix[others_edges[i]][edge[0]]
        point1_y1 = right_lim_x + full_path_matrix[others_edges[i]][edge[0]]

        point2_y0 = weight + full_path_matrix[others_edges[i]][edge[1]] - left_lim_x
        point2_y1 = weight + full_path_matrix[others_edges[i]][edge[1]] - right_lim_x

        name = (f"d(f, {others_edges[i]}) = (x + {full_path_matrix[others_edges[i]][edge[0]]} ; "
                f"{weight + full_path_matrix[others_edges[i]][edge[1]]} - x)")

        plot = graph.show_graph(point1_y0, left_lim_x, point1_y1, right_lim_x,
                                point2_y0, left_lim_x, point2_y1, right_lim_x,
                                left_lim_x, right_lim_x, name)

        point1 = [left_lim_x, point1_y0]
        point2 = [right_lim_x, point1_y1]

        point3 = [left_lim_x, point2_y0]
        point4 = [right_lim_x, point2_y1]

        x_inter, y_inter = (find_line_intersection((point1, point2), (point3, point4)))

        if y_inter >= point1_y0:
            all_pointers.append(([left_lim_x, point1_y0], [x_inter, y_inter]))
        if y_inter >= point1_y1:
            all_pointers.append(([right_lim_x, point1_y1], [x_inter, y_inter]))
        if y_inter >= point2_y0:
            all_pointers.append(([left_lim_x, point2_y0], [x_inter, y_inter]))
        if y_inter >= point2_y1:
            all_pointers.append(([right_lim_x, point2_y1], [x_inter, y_inter]))

    all_pointers = delete_duplicates(all_pointers)

    return all_pointers, plot


def get_mark(matrix: TMatrix,
             edges: list[TEdge]) -> (int, TEdge):
    marks = [max(min(elem1, elem2) for index, (elem1, elem2) in enumerate(zip(matrix[i], matrix[j]))) for i, j in edges]

    return min(marks), edges[marks.index(min(marks))]


def find_edges(matrix: TMatrix) -> list[TEdge]:
    edges = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < j and matrix[i][j] != 0:
                edges.append((i, j))

    return edges


def solve(matrix: TMatrix) -> None:
    showinfo(title="Warning", message="Numbering in edges starts from 0")

    edges = find_edges(matrix)
    full_path_matrix = find_full_path_matrix(matrix)
    min_mark, edge = get_mark(full_path_matrix, edges)

    others_edges = [_ for _ in range(len(full_path_matrix)) if _ not in edge]
    weight = full_path_matrix[edge[0]][edge[1]]

    all_pointers, plot = find_points_on_graph(others_edges, weight, full_path_matrix, edge)
    plot = graph.show_final_graph(all_pointers, 0, weight, plot)
    plot.show()
