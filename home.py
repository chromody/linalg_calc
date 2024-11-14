import customtkinter as ctk

def create_home_page(root):
    home_frame = ctk.CTkFrame(master=root)

    # Title label
    home_label = ctk.CTkLabel(home_frame, text="Welcome to Linear Algebra Calculator", font=("Arial", 24))
    home_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

    # Description label
    description = ctk.CTkLabel(home_frame, text="A tool to help you with matrix and vector operations.\nSelect a tool from the menu above to begin.", font=("Arial", 16))
    description.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

    # Instructions label
    instructions = ctk.CTkLabel(home_frame, text="Use the Operations menu to choose a calculator.", font=("Arial", 14))
    instructions.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

    # Configure row and column weights for centering in the middle of the window
    home_frame.grid_rowconfigure(0, weight=1)
    home_frame.grid_rowconfigure(1, weight=1)
    home_frame.grid_rowconfigure(2, weight=1)
    home_frame.grid_columnconfigure(0, weight=1)
    home_frame.grid_columnconfigure(1, weight=1)

    # Center the frame in the middle
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    home_frame.grid(row=0, column=0, padx=10, pady=10)

    return home_frame
