#! /usr/bin/env python3

class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self.days += 1


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    plants = [rose, oak, cactus, sunflower, fern]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
