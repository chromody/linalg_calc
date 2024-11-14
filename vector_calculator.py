import customtkinter as ctk

def create_vector_calculator_page(root):
    vector_calculator_frame = ctk.CTkFrame(master=root)
    vector_label = ctk.CTkLabel(vector_calculator_frame, text="Vector Calculator", font=("Arial", 24))
    vector_label.grid(row=0, column=0, padx=10, pady=10)
    return vector_calculator_frame
