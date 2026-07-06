#!/usr/bin/env python3

import random

PLAYERS = [
    "Alice", "bob", "Charlie", "dylan", "Emma",
    "Gregory", "john", "kevin", "Liam"
]


def main() -> None:
    first_comprehension = [x for x in PLAYERS if x.istitle()]
    second_comprehension = [x.capitalize() for x in PLAYERS]

    dict_c = {name: random.randint(0, 1000) for name in second_comprehension}
    average = sum(dict_c.values()) / len(dict_c)
    average_two = round(average, 2)

    highest = {
        name: score for name, score in dict_c.items() if score > average
    }

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {PLAYERS}")
    print(f"New list with all names capitalized: {second_comprehension}")
    print(f"New list of capitalized names only: {first_comprehension}\n")
    print(f"Score dict: {dict_c}")
    print(f"Score average is {average_two}")
    print(f"High scores: {highest}")


if __name__ == "__main__":
    main()
