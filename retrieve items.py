import sys
import tkinter as tk
from tkinter import messagebox, simpledialog

class Item:
    def __init__(self, name, description, contact_info):
        self.name = name
        self.description = description
        self.contact_info = contact_info

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nContact Info: {self.contact_info}\n"


class ReviveItems:
    def __init__(self):
        self.items = []

    def add_item(self, name, description, contact_info):
        item = Item(name, description, contact_info)
        self.items.append(item)
        return f"Item '{name}' has been added."

    def delete_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return f"Item '{name}' has been deleted."
        return f"Item '{name}' is not found."

    def show_items(self):
        if not self.items:
            return "No items now."
        else:
            return "\n".join(str(item) for item in self.items)

    def find_item(self, name):
        for item in self.items:
            if item.name == name:
                return str(item)
        return f"Item '{name}' is not found."


class GUIApp:
    def __init__(self, root):
        self.revive_items = ReviveItems()
        self.root = root
        self.root.title("Revive Items Manager")

        # Main label
        self.label = tk.Label(root, text="Revive Items Manager", font=("Arial", 16))
        self.label.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Item", command=self.delete_item)
        self.delete_button.pack(pady=5)

        self.show_button = tk.Button(root, text="Show All Items", command=self.show_items)
        self.show_button.pack(pady=5)

        self.find_button = tk.Button(root, text="Find Item", command=self.find_item)
        self.find_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)

        # Output text box
        self.output_text = tk.Text(root, width=50, height=15)
        self.output_text.pack(pady=10)

    def add_item(self):
        name = simpledialog.askstring("Add Item", "Please enter your item name:")
        if name:
            description = simpledialog.askstring("Add Item", "Please enter your item description:")
            contact_info = simpledialog.askstring("Add Item", "Please enter your item's contact information:")
            result = self.revive_items.add_item(name, description, contact_info)
            self.output_text.insert(tk.END, result + "\n")

    def delete_item(self):
        name = simpledialog.askstring("Delete Item", "Please enter the name of the item you want to delete:")
        if name:
            result = self.revive_items.delete_item(name)
            self.output_text.insert(tk.END, result + "\n")

    def show_items(self):
        result = self.revive_items.show_items()
        self.output_text.insert(tk.END, result + "\n")

    def find_item(self):
        name = simpledialog.askstring("Find Item", "Please enter the name of the item you want to find:")
        if name:
            result = self.revive_items.find_item(name)
            self.output_text.insert(tk.END, result + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()

