import tkinter as tk
from tkinter import simpledialog
import keyboard
from tkinter import ttk

class ControllerConfigurator:
    def __init__(self, master):
        self.master = master
        master.title("gptlmk v0.1 alpha test ver")

        self.key_mappings = {}  # Dictionary to store key mappings

        # Set a modern Tkinter theme
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.create_table()
        self.create_generate_button()

    def create_table(self):
        table_frame = ttk.Frame(self.master)
        table_frame.pack()

        columns = ["Action", "Assigned Key"]

        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.column("Action", width=150)
        self.tree.column("Assigned Key", width=150)

        actions = [
            "Start", "Guide","Select", "A", "B", "X", "Y",
            "L1", "L2", "L3", "R1", "R2", "R3",
            "Up", "Down", "Left", "Right",
            "Left Analog Up", "Left Analog Down", "Left Analog Left", "Left Analog Right",
            "Right Analog Up", "Right Analog Down", "Right Analog Left", "Right Analog Right"
        ]

        for action in actions:
            self.tree.insert("", "end", values=(action, "None"))

        self.tree.pack()

        assign_button = ttk.Button(self.master, text="Assign Key", command=self.assign_selected_key)
        assign_button.pack(pady=10)

    def create_generate_button(self):
        generate_button = ttk.Button(self.master, text="Generate .gptk File", command=self.generate_gptk_file)
        generate_button.pack(pady=10)

    def assign_key(self, action):
        # Use a dialog to get user input for key assignment
        key = simpledialog.askstring("Key Assignment", f"Assign a key for {action}")

        if key:
            # Register a hotkey for the assigned key and associate it with the action
            try:
                keyboard.add_hotkey(key, lambda a=action: self.perform_action(a))
            except:
                print("Warning: You Not add key!")
            self.key_mappings[action] = key  # Store the key mapping
            print(f"Key {key} assigned for {action}")
            self.update_table()

    def assign_selected_key(self):
        selected_item = self.tree.selection()
        if selected_item:
            action = self.tree.item(selected_item, 'values')[0]
            self.assign_key(action)

    def perform_action(self, action):
        # Replace this with your logic to perform the action associated with the key
        print(f"Performing action: {action}")

    def update_table(self):
        for action, key in self.key_mappings.items():
            for child in self.tree.get_children():
                if self.tree.item(child, 'values')[0] == action:
                    self.tree.item(child, values=(action, key))
                    break

    def generate_gptk_file(self):
        with open("remap.gptk", "w") as file:
            file.write("# Remap Configuration Made By GPTKMK\n\n")

            for action, key in self.key_mappings.items():
                file.write(f"{str(action).lower().replace(' ', '_')} = {str(key).lower()}\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = ControllerConfigurator(root)
    root.mainloop()
