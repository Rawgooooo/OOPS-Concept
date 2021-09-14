
"""
Polymorphism
Polymorphism simply means having many forms.
For example, we need to determine if the given species of birds fly or not,
using polymorphism we can do this using a single function."""

class OnePiece:
    def intro(self):
        print("There are many types of characters.")

    def evilFruit(self):
        print("Some have eaten EVIL FRUITS while some haven't\n")

class Luffy(OnePiece):
    def evilFruit(self):
        print("Luffy ate Gomu-Gomu fruit.")

class Shanks(OnePiece):
    def evilFruit(self):
        print("Shanks hasn't eaten any EVIL FRUIT.")

anime_OP = OnePiece()
person_Luffy = Luffy()
person_Shanks = Shanks()

anime_OP.intro()
anime_OP.evilFruit()

person_Luffy.evilFruit()
person_Shanks.evilFruit()

