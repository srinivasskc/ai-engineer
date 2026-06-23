import random


class Person:
    def __init__(self, firstName, lastName, health, status):
        """Initialize attributes to be used in/available for all class methods in this class"""
        self.firstName = firstName
        self.lastName = lastName
        self.health = health
        self.status = status

    def introduce(self):
        """
        To introduce each person themselves.
        """
        print(f"Hello, my name is {self.firstName}, {self.lastName}")

    def emotion(self):
        """ """
        emotion = random.randrange(1, 3)

        if self.emotion == 1:
            print(f"{self.firstName} is happy")
        elif self.emotion == 2:
            print(f"{self.firstName} is not happy")
        else:
            print(f"{self.firstName} is sad")

    def status_check(self):
        if self.health == 100:
            print(f"{self.firstName} is healthy")
        elif self.health >= 76 and self.health <= 99:
            print(f"{self.firstName} is doing well")
        elif self.health >= 51 and self.health <= 75:
            print(f"{self.firstName} is not well")
        elif self.health >= 41 and self.health <= 50:
            print(f"{self.firstName} need to visit doctor")
        else:
            print(f"{self.firstName} is unconsicousness")


Srinivas = Person("Srinivas", "Kadiyala", 75, status=True)
Vasu = Person("Vasu", "Kadiyala", 100, status=False)

print(f"{Srinivas.firstName} is my friend? {Srinivas.status}")
print(f"{Vasu.firstName} is my friend? {Vasu.status}")


Srinivas.introduce()
Vasu.introduce()

Srinivas.status_check()
Vasu.status_check()
