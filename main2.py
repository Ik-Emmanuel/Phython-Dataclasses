from dataclasses import dataclass, field

@dataclass(order=True) #allows you compare different class instance
class Person:
    sort_index: int = field(init=False, repr=False) #allow you sort by a given attribute 
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        # self.sort_index = self.age
        object.__setattr__(self, 'sort_index', self.strength) #for frozen dataclasses

person1 = Person("Kelly", "Clarkson", 20)
person2 = Person("Joe", "Regan", 30, 200)
person3 = Person("Melly", "Buns", 40)

print(person2)
print(person3)

print(person2 > person3)