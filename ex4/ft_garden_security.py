#! /usr/bin/env python3

class Plant:
    def __init__(self, name, height, days):
        self._name = name
        self._height = height
        self._days = days
        self._growth_rate = 1

    def show(self):
        return (f"{self._name}:"
                f" {round(self._height, 1)}cm, {self._days} days old")

    def grow(self):
        self._height += self._growth_rate

    def age(self):
        self._days += 1

    def set_height(self, value):
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = value

    def set_age(self, value):
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._days = value

    def get_height(self):
        return self._height

    def get_age(self):
        return self._days


def main() -> None:
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print(f"Plant created: {rose.show()}")
    print()
    rose.set_height(25)
    print("Height updated: 25cm")
    rose.set_age(30)
    print("Age updated: 30 days\n")
    rose.set_height(-5)
    print("Height update rejected")
    rose.set_age(-3)
    print("Age update rejected\n")
    print(f"Current state: {rose.show()}")


if __name__ == "__main__":
    main()
