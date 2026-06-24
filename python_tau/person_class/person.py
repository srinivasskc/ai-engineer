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
        emotion = random.randrange(1, 4)

        if emotion == 1:
            print(f"{self.firstName} is happy")
        elif emotion == 2:
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


Srinivas = Person("Srinivas", "Kadiyala", 95, status=True)
Vasu = Person("Vasu", "Kadiyala", 70, status=False)

print(f"{Srinivas.firstName} is my friend? {Srinivas.status}")
print(f"{Vasu.firstName} is my friend? {Vasu.status}")


Srinivas.introduce()
Vasu.introduce()

Srinivas.status_check()
Vasu.status_check()


Srinivas.emotion()
Vasu.emotion()


# Inheritance - Inheriting Person Class to Enemy Class.
class Enemy(Person):
    def __init__(self, weapon, firstName, lastName, health, status):
        super().__init__(firstName, lastName, health, status)
        self.weapon = weapon

    # Polymorphism - Method Overriding
    def introduce(self):
        print("You are my mortal enemy!!")

    # Here self is Self Person, other is Other hurting-> person/insult person.
    def hurt(self, other):
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "stick":
            other.health -= 5
        print(f"Now, {other.firstName} health score is:  {other.health}")

    def insult(self, other):
        if other.health <= 80:
            print(f"{other.firstName} you are tired and weak")


print("====Now, with Alex=====")

Alex = Enemy("rock", "Alex", "Max", 75, status=False)
Alex.hurt(Srinivas)
Alex.insult(Srinivas)
Alex.insult(Vasu)

print("====Now, with Matt=====")


Matt = Enemy("stick", "Matt", "Hutt", 85, status=True)
Matt.hurt(Srinivas)
Matt.insult(Srinivas)
Matt.insult(Vasu)

print("====Calling Polymorphism method-Enemey===")
Alex.introduce()
