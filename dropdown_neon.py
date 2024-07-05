import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  

class NeonDropdownMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Neon Dropdown Menu")
        self.root.geometry("400x200")
        self.root.configure(bg="#FFB6C1")  

        self.label = tk.Label(root, text="Select an option:", font=("Arial", 14), bg="#000000", fg="#00FF00") 
        self.label.pack(pady=20)

        neon_style = ttk.Style()
        neon_style.theme_use('clam')
        neon_style.configure('TCombobox', 
                             fieldbackground='#000000',  
                             background='#000000',      
                             foreground='#00FF00',
                             selectbackground='#00FF00',
                             selectforeground='#000000', 
                             arrowcolor='#00FF00') 

        self.options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        self.selected_option = tk.StringVar()

        self.dropdown = ttk.Combobox(root, values=self.options, textvariable=self.selected_option, style='TCombobox', font=("Arial", 12))
        self.dropdown.pack(pady=10)

        self.button = tk.Button(root, text="Submit", font=("Arial", 12), bg="#00FF00", fg="#000000", command=self.submit)
        self.button.pack(pady=20)

    def submit(self):
        selected = self.selected_option.get()
        messagebox.showinfo("Selection", f"You selected: {selected}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NeonDropdownMenu(root)
    root.mainloop()
