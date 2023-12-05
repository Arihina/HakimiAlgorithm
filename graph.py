from typing import TypeVar

import matplotlib.pyplot as plt

TPyplot = TypeVar("TPyplot", bound=plt)


def show_graph(x1: int | float, y1: int | float,
               x2: int | float, y2: int | float,
               x3: int | float, y3: int | float,
               x4: int | float, y4: int | float,
               vertical_x1: int | float, vertical_x2: int | float, graph_name: str) -> TPyplot:
    plt.figure(graph_name)

    plt.axvline(x=vertical_x1)
    plt.axvline(x=vertical_x2)

    px1, py1 = [y1, y2], [x1, x2]
    px2, py2 = [y3, y4], [x3, x4]

    plt.plot(px1, py1, px2, py2, marker='o')

    return plt


def show_final_graph(lst: list[tuple[list[int | float, int | float], list[int | float, int | float]]],
                     vertical_x1: int | float, vertical_x2: int | float) -> TPyplot:
    plt.figure()

    plt.axvline(x=vertical_x1)
    plt.axvline(x=vertical_x2)

    for i in range(len(lst)):
        point1, point2 = lst[i]
        x1, y1 = point1
        x2, y2 = point2
        x_point = [x1, x2]
        y_point = [y1, y2]
        plt.plot(x_point, y_point)

    return plt
