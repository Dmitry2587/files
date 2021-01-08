class BaseAnimal:
    paws = 4


class Animal(BaseAnimal):

    def __init__(self, name):
        self.name = name

    def say(self, phrase):
        print(phrase)

animal = BaseAnimal()
print(animal.paws)

dog = Animal("Sharik")
print(dog.paws)
spider = Animal(name="Glazik")
print(spider.paws)


# print(dog.name)
# print(spider.name)
# print(Animal.name)
