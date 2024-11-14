import tkinter as tk #using tkinter and customtkinter for our gui
import customtkinter as ctk
from matrix_calculator import create_matrix_calculator_page #splitting our "pages" into their respective files, for scalability
from vector_calculator import create_vector_calculator_page
import json #we use json and os for appearance preferences
import os
from CTkMessagebox import CTkMessagebox

def show_about():
    CTkMessagebox(title="About", message="This is a basic linear algebra calculator.")


def change_appearance_mode(new_mode: str): #change the appearance mode
    ctk.set_appearance_mode(new_mode)
    save_appearance_mode(new_mode)

def save_appearance_mode(mode):
    with open("settings.json", "w") as f:
        json.dump({"appearance_mode": mode}, f)

def load_appearance_mode():
    if os.path.exists("settings.json"):
        with open("settings.json", "r") as f:
            settings = json.load(f)
            return settings.get("appearance_mode", "light")
    return "light"  # Default to light mode if no saved preference

def show_matrix_calculator():
    hide_all_frames()
    matrix_calculator_frame.grid(row=0, column=0, padx=10, pady=10)

def show_vector_calculator():
    hide_all_frames()
    vector_calculator_frame.grid(row=0, column=0, padx=10, pady=10)

def hide_all_frames():
    matrix_calculator_frame.grid_forget()
    vector_calculator_frame.grid_forget()

# Initialize main window
root = ctk.CTk()
root.title("Linear Algebra Calculator")
root.geometry("600x400")

# Load the saved appearance mode
initial_mode = load_appearance_mode()
ctk.set_appearance_mode(initial_mode)
ctk.set_default_color_theme("dark-blue")

# Create the initial frames (pages)
matrix_calculator_frame = create_matrix_calculator_page(root)
vector_calculator_frame = create_vector_calculator_page(root)

# Create the top menu using Tkinter's Menu class
menu_bar = tk.Menu(root)

# File menu with dropdown
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Operations menu with dropdown
operations_menu = tk.Menu(menu_bar, tearoff=0)
operations_menu.add_command(label="Matrix Calculator", command=show_matrix_calculator)
operations_menu.add_command(label="Vector Calculator", command=show_vector_calculator)
menu_bar.add_cascade(label="Operations", menu=operations_menu)

# Dark Mode, Light Mode, and System menu
appearance_menu = tk.Menu(menu_bar, tearoff=0)
appearance_menu.add_command(label="Light Mode", command=lambda: change_appearance_mode("light"))
appearance_menu.add_command(label="Dark Mode", command=lambda: change_appearance_mode("dark"))
appearance_menu.add_command(label="System", command=lambda: change_appearance_mode("system"))
menu_bar.add_cascade(label="Appearance", menu=appearance_menu)

# Help menu with an About option
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the menu bar
root.config(menu=menu_bar)

# Start the application
root.mainloop()
