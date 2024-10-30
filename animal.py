class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Cat(Animal):
    def __init__(self, name, sound, breed, color):
        super().__init__(name, sound)
        self.breed = breed
        self.color = color

    def make_sound(self):
        print(self.name, self.sound)

    def description(self):
        print(self.color)

class Dog(Animal):
    def __init__(self, name, sound, breed, color):
        super().__init__(name, sound)
        self.breed = breed
        self.color = color

    def make_sound(self):
        print(self.name, self.sound)

    def description(self):
        print(self.color)

cat1 = Cat("Kitty", "Meow-meow", "Ragdoll", "Black")
cat1.make_sound()
cat1.description()

dog1 = Dog("Doggy", "Bark-bark", "Golden Retriever", "Golden")
dog1.make_sound()
dog1.description()