#!/usr/bin/env python3

import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:
        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name, quantity_s = parts

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantity = int(quantity_s)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue

        inventory[name] = quantity

    return inventory


def main() -> None:
    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    item_numbers = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {item_numbers}")

    for name, quantity in inventory.items():
        pourcentage = (quantity / item_numbers) * 100
        print(f"Item {name} represents {round(pourcentage, 1)}%")

    most_name, most_qty = None, None
    least_name, least_qty = None, None

    for name, quantity in inventory.items():
        if most_qty is None or quantity > most_qty:
            most_name, most_qty = name, quantity
        if least_qty is None or quantity < least_qty:
            least_name, least_qty = name, quantity

    print(f"Item most abundant: {most_name} with quantity {most_qty}")
    print(f"Item least abundant: {least_name} with quantity {least_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
