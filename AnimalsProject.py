class Farm_Animals:
    place = "farm"

class Bird(Farm_Animals):
    beak = "beak"
    def __init__(self, wings, legs):
        self.wings = wings
        self.legs = legs

class Ungulates(Farm_Animals):
    hoofs = "hoofs"
    horns = "horns"
    def __init__(self, legs):
        self.legs = legs

class Cow(Ungulates):
    name = "Cow"
    sound = "Moo!"
class Pig(Ungulates):
    name = "Pig"
    sound = "Oink!"
class Sheep(Ungulates):
    name = "Sheep"
    sound = "Mee!"
class Goat(Ungulates):
    name = "Goat"
    sound = "Bee!"

class Chicken(Bird):
    name = "Chicken"
    sound = "Cluck!"
class Goose(Bird):
    name = "Goose"
    sound = "Cackle!"
class Duck(Bird):
    name = "Duck"
    sound = "Quack!"


chicken = Chicken(2, 2)
goose = Goose(2, 2)
duck = Duck(2, 2)
print("")
print("%s lives on %s. It has %s, %s wings and %s legs. %s says %s" % (chicken.name, chicken.place, chicken.beak, chicken.wings, chicken.legs, chicken.name, chicken.sound))
print("%s lives on %s. It has %s, %s wings and %s legs. %s says %s" % (goose.name, goose.place, goose.beak, goose.wings, goose.legs, goose.name, goose.sound))
print("%s lives on %s. It has %s, %s wings and %s legs. %s says %s" % (duck.name, duck.place, duck.beak, duck.wings, duck.legs, duck.name, duck.sound))



cow = Cow(4)
goat = Goat(4)
pig = Pig(4)
sheep = Sheep(4)
print("")
print("%s lives on %s. It has %s legs, %s and %s. %s says %s" % (cow.name, cow.place, cow.legs, cow.horns, cow.hoofs, cow.name, cow.sound))
print("%s lives on %s. It has %s legs, %s and %s. %s says %s" % (goat.name, goat.place, goat.legs, goat.horns, goat.hoofs, goat.name, goat.sound))
print("%s lives on %s. It has %s legs and %s, bit it doesn't have %s. %s says %s" % (pig.name, pig.place, pig.legs, pig.hoofs, pig.horns, pig.name, pig.sound))
print("%s lives on %s. It has %s legs and %s, bit it doesn't have %s. %s says %s" % (sheep.name, sheep.place, sheep.legs, sheep.hoofs, sheep.horns, sheep.name, sheep.sound))
