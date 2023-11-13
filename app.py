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

        actions = [
            "Start", "Guide","Select", "A", "B", "X", "Y",
            "L1", "L2", "L3", "R1", "R2", "R3",
            "Up", "Down", "Left", "Right",
            "Left Analog Up", "Left Analog Down", "Left Analog Left", "Left Analog Right",
            "Right Analog Up", "Right Analog Down", "Right Analog Left", "Right Analog Right"
        ]

        for action in actions:
            row_frame = ttk.Frame(table_frame)
            row_frame.pack(side=tk.TOP)

            label = ttk.Label(row_frame, text=action)
            label.pack(side=tk.LEFT)

            key_button = ttk.Button(row_frame, text="Assign Key", command=lambda a=action: self.assign_key(a))
            key_button.pack(side=tk.LEFT)

    def create_generate_button(self):
        generate_button = ttk.Button(self.master, text="Generate .gptk File", command=self.generate_gptk_file)
        generate_button.pack(pady=10)

    def assign_key(self, action):
        # Use a dialog to get user input for key assignment
        key = simpledialog.askstring("Key Assignment", f"Assign a key for {action}")

        if key:
            # Register a hotkey for the assigned key and associate it with the action
            keyboard.add_hotkey(key, lambda a=action: self.perform_action(a))
            self.key_mappings[action] = key  # Store the key mapping
            print(f"Key {key} assigned for {action}")

    def perform_action(self, action):
        # Replace this with your logic to perform the action associated with the key
        print(f"Performing action: {action}")

    def generate_gptk_file(self):
        with open("remap.gptk", "w") as file:
            file.write("# Remap Configuration Made By GPTKMK\n\n")

            for action, key in self.key_mappings.items():
                file.write(f"{str(action).lower().replace(" ", "_")} = {str(key).lower()}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ControllerConfigurator(root)
    root.mainloop()
