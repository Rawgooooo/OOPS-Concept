
# class name
class Pokemon:

    # class attribute
    """attributes mentioned here apply for the whole class"""
    rarity = "legendary"

    # Instance attribute
    """attributes here are applicable only for the unique object"""
    def __init__(self, name):
        self.name = name

    # method
    def speak(self):
        print(f"My name is {self.name}")

Xerneas = Pokemon("Xerneas")
Darkrai = Pokemon("Darkrai")

print(f"Xerneas is a {Xerneas.__class__.rarity} pokemon!")
print(f"Darkrai is a {Xerneas.__class__.rarity} pokemon!")

Darkrai.speak()
Xerneas.speak()
