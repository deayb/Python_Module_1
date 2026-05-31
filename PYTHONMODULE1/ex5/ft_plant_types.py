#! /usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days
        self._growth_rate = 2.1

    def show(self) -> None:
        print(f"{self._name}:"
              f" {round(self._height, 1)}cm, {self._days} days old")

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._days += 1

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._days = value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days: int, color: str) -> None:
        super().__init__(name=name, height=height, days=days)
        self._color = color
        self._blooming = False

    def bloom(self) -> None:
        self._blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days: int, diameter: float) -> None:
        super().__init__(name=name, height=height, days=days)
        self._diameter = diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of"
              f" {self._height}cm long and {self._diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days: int, harvest_season: str) -> None:
        super().__init__(name=name, height=height, days=days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
