#! /usr/bin/env python3

class Plant:
    def __init__(self):
        self.name = ""
        self.height = 0
        self.days = 0
        self.growth_rate = 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self.days += 1


def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days = 30
    rose.growth_rate = 0.8

    hauteur_depart = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()
    for jour in range(7):
        print(f"=== Day {jour + 1} ===")
        rose.grow()
        rose.age()
        rose.show()

    print(f"Growth this week: {round(rose.height - hauteur_depart, 1)}cm")


if __name__ == "__main__":
    main()
