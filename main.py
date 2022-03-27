import random 
import string 
from dataclasses import dataclass, field

def generate_id() -> str:
    """ A function that simply generates a random string of certain length"""
    return "".join(random.choices(string.ascii_uppercase, k=12))

# #old inefficient way of class definition 
# class Person:
#     def __init__(self, name: str, address: str):
#         self.name = name
#         self.address = address
    
#     def __str__(self) -> str:
#         return f"{self.name}, {self.address}"


@dataclass
# @dataclass(frozen=True)
# @dataclass(kw_only=True) #for python 3.10+
class Person:
    name: str
    address: str
    active: bool = True #default values for primitive types
    email_addresses: list[str] = field(default_factory=list) #default values for non primitive types
    id: str = field(default_factory=generate_id, init=False) #init=False specifies that this field should not be part of the initializer for the instance 
    _search_string : str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """
        post_init methods are used to generate other class variables after instance initialization. helps augment the object with extra generated data after initialization
        """
        self._search_string = f"{self.name}-{self.address}"

    #it auto generates an initializer and __repr__ method for the class 

   
def main() -> None:
    person = Person(name="Micheal", address="4b west avenue", active=False)
    print(person)


if __name__=="__main__":
    main()