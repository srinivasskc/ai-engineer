## Multiple Inheritance

# Parent Class 1


class Item:
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print(f"The sku is {self.sku} units")


# Parent Class 2


class Garment:
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print(f"The garment is of {self.type} and is in {self.section} section")


# Child Class - Inheriting from both parents.
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print(f"The shirt color is {self.color} and is of brand {self.name}")


intune_shirts = Shirts("100", "shirts", "cotton", "intune", "blue")
intune_shirts.print_sku()
intune_shirts.print_garment()
intune_shirts.print_shirt()
