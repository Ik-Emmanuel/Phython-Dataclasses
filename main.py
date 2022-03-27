import random 
import string 


def generate_id() -> str:
    """ A function that simply generates a random string of certain length"""
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
    
    def __str__(self) -> str:
        return f"{self.name}, {self.address}"


def main() -> None:
    person = Person(name="Micheal", address="4b west avenue")
    print(person)


if __name__=="__main__":
    main()