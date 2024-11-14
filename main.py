import tkinter as tk
import customtkinter as ctk

# Create the main application window
root = ctk.CTk()  # Use CTk instead of Tk() for a customtkinter window
root.title("CustomTkinter Example")  # Set the title of the window
root.geometry("400x300")  # Set the window size

# Add a label
label = ctk.CTkLabel(root, text="Hello, CustomTkinter!", font=("Arial", 20))
label.pack(pady=20)

# Add a button that changes the label text
def change_text():
    label.configure(text="You clicked the button!")  # Use 'configure' instead of 'config'

button = ctk.CTkButton(root, text="Click Me", command=change_text)
button.pack(pady=10)

# Start the application
root.mainloop()
