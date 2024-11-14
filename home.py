import customtkinter as ctk

def create_home_page(root):
    home_frame = ctk.CTkFrame(master=root)
    home_label = ctk.CTkLabel(home_frame, text="Home Page", font=("Arial", 24))
    home_label.grid(row=0, column=0, padx=10, pady=10)
    return home_frame
