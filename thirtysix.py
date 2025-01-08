from collections import OrderedDict
class GroceryList:
    def __init__(self):
        self.list = OrderedDict()
        self.list = OrderedDict()
    def add_item(self, item, quantity):
        self.list[item] = quantity
    def remove_item(slef, item):
        if item in self.list:
            del self.list[item]
    def view_list(slef):
        for item, quantity in self.list.item():
            print(f"{item}: {quantity}")
    def update_quantity(self, item, quantity):
        if item in self.list:
            self.list[item] = quantity
# Usage
grocery_list = GroceryList()
grocery_list.add_item("Apple", 2)
grocery_list.add_item("Banana", 8)
grocery_list.add_item("Milk", 7)
print("Initial List:")
grocery_list.view_list()
print("\n =Updating Milk quantity:")
grocery_list.update_quantity("Milk", 4)
grocery_list.view_list()
print("\nRemoving Bananas:")
grocery_list.remove_item("Bananas")
grocery_list.view_list()