from typing import TypeVar

import customtkinter as ctk
import matplotlib.pyplot as plt

TPyplot = TypeVar("TPyplot", bound=plt)

TTupleList = TypeVar("TTupleList",
                     bound=
                     list[tuple[list[int | float, int | float], list[int | float, int | float]]])

TPointsTuple = TypeVar("TPointsTuple", bound=tuple[list[int | float], list[int | float | list[int | float]]])

TMatrix = TypeVar("TMatrix", bound=list[list[int | float]])

TEdge = TypeVar("TEdge", bound=tuple[int, int])

TWindow = TypeVar("TWindow", bound=ctk.CTk)

TLabel = TypeVar("TLabel", bound=ctk.CTkLabel)

TEntry = TypeVar("TEntry", bound=ctk.CTkEntry)

TButton = TypeVar("TButton", bound=ctk.CTkButton)
