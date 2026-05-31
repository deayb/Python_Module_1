#! /usr/bin/env python3

class Plant:
    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, "
                  f"{self._show_count} show")

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days
        self._growth_rate = 2.1
        self._stats = Plant.Stats()

    def show(self) -> None:
        print(f"{self._name}:"
              f" {round(self._height, 1)}cm, {self._days} days old")
        self._stats._show_count += 1

    def grow(self) -> None:
        self._height += self._growth_rate
        self._stats._grow_count += 1

    def age(self) -> None:
        self._days += 1
        self._stats._age_count += 1

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
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

    def __init__(self, name: str, height: float,
                 days: int, diameter: float) -> None:
        super().__init__(name=name, height=height, days=days)
        self._diameter = diameter
        self._stats: Tree.TreeStats = Tree.TreeStats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of"
              f" {self._height}cm long and {self._diameter}cm wide.")
        self._stats._shade_count += 1


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


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 days: int, color: str) -> None:
        super().__init__(name, height, days, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


def display_stats(plant: Plant) -> None:
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year?"
          f" -> {Plant.is_older_than_a_year(400)}\n")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print()

    print("=== Anonymous")
    anonym = Plant.create_anonymous()
    anonym.show()
    print("[statistics for Unknown plant]")
    display_stats(anonym)
