from tkinter.messagebox import showerror
import customtkinter as ctk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

MATRIX = None


def start_solve(fields: list, size: int, root) -> None:
    try:
        matrix = read_load_matrix(fields, size)
        global MATRIX
        MATRIX = matrix
        root.quit()
    except ValueError:
        return


def read_load_matrix(fields: list, size: int) -> list[list[float]]:
    matrix = []
    row = []
    count_elem = 0

    for field in fields:
        try:
            row.append(float(field.get()))
            count_elem += 1
        except ValueError:
            showerror(title="Error", message="Check the correctness of the input")
            raise ValueError

        if count_elem == size:
            matrix.append(row)
            row = []
            count_elem = 0

    return matrix


def draw_entry_matrix(size: int, root) -> list:
    fields = []
    frame = ctk.CTkFrame(root)
    frame.grid(row=1, column=0, columnspan=size)

    for i in range(size):
        for j in range(size):
            field = ctk.CTkEntry(frame, font=ctk.CTkFont(size=20), width=35)
            field.grid(row=i, column=j, pady=(3, 3), padx=(3, 3))
            fields.append(field)

    return fields


def redraw_root(size: str, root, label, entry, button) -> None:
    try:
        size = int(size)
    except ValueError:
        showerror(title="Error", message="Check the correctness of the input")
        return

    entry.destroy()
    label.configure(text="Enter the load matrix")
    label.grid(columnspan=size)
    button.grid(columnspan=size, row=2)

    fields = draw_entry_matrix(size, root)

    button.configure(command=lambda: start_solve(fields, size, root))


def run() -> None:
    root = ctk.CTk()
    root.title("Hakimi")

    label = ctk.CTkLabel(root, text="Enter the number of nodes in the graph", font=ctk.CTkFont(size=20))
    label.grid(row=0, column=0, pady=(20, 20), padx=(20, 20))

    entry = ctk.CTkEntry(root, font=ctk.CTkFont(size=20))
    entry.grid(row=1, column=0, pady=(20, 20), padx=(20, 20))

    button = ctk.CTkButton(root, text="Next", command=lambda: redraw_root(entry.get(), root, label, entry, button),
                           font=ctk.CTkFont(size=20))
    button.grid(row=2, column=0, pady=(20, 20), padx=(20, 20))

    root.mainloop()
