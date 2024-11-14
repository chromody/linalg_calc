import customtkinter as ctk

def create_matrix_calculator_page(root):
    matrix_calculator_frame = ctk.CTkFrame(master=root)
    matrix_label = ctk.CTkLabel(matrix_calculator_frame, text="Matrix Calculator", font=("Arial", 24))
    matrix_label.grid(row=0, column=0, padx=10, pady=10)
    return matrix_calculator_frame
