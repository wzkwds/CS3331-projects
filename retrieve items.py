import sys

class Item:
    def __init__(self, name, description, contact_info):
        self.name = name
        self.description = description
        self.contact_info = contact_info

    def __str__(self):
        return f"name: {self.name}\ndescription: {self.description}\ncontact_info:{self.contact_info}\n"


class ReviveItems:
    def __init__(self):
        self.items = []

    def add_item(self, name, description, contact_info):
        item = Item(name, description, contact_info)
        self.items.append(item)
        print(f"item'{name}'has been added.\n")

    def delete_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"item'{name}'has been deleted.\n")
                return
        print(f"item'{name}'is not found.\n")

    def show_items(self):
        if not self.items:
            print("no item now.\n")
        else:
            for item in self.items:
                print(item)

    def find_item(self, name):
        for item in self.items:
            if item.name == name:
                print(item)
                return
        print(f"item'{name}'is not found.\n")


def main():
    revive_items = ReviveItems()

    while True:
        print("command options:")
        print("1. add item")
        print("2. delete item")
        print("3. show all items")
        print("4. find item")
        print("5. exit")

        choice = input("your choice: ")

        if choice == "1":
            name = input("enter your item name: ")
            description = input("enter your item description: ")
            contact_info = input("enter your item's contact information: ")
            revive_items.add_item(name, description, contact_info)
        elif choice == "2":
            name = input("enter the name of item you want to delete: ")
            revive_items.delete_item(name)
        elif choice == "3":
            revive_items.show_items()
        elif choice == "4":
            name = input("enter the name of item you want to find: ")
            revive_items.find_item(name)
        elif choice == "5":
            print("exit the program.")
            sys.exit()
        else:
            print("not available command, please retry other commands.\n")


if __name__ == "__main__":
    main()
