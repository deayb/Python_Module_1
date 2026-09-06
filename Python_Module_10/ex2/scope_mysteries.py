from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count = count + 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    final = initial_power

    def accumulation(amount: int) -> int:
        nonlocal final
        final = final + amount
        return final
    return accumulation


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memories = {}

    def store(key: str, value: Any) -> None:
        memories[key] = value

    def recall(key: str) -> Any:
        if key not in memories:
            return "Memory not found"
        return memories[key]

    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    base_number = spell_accumulator(100)
    print(f"Base 100, add 20: {base_number(20)}")
    print(f"Base 100, add 30: {base_number(30)}")

    print("\nTesting enchantment factory...")
    enchantment_1 = enchantment_factory('Flaming')
    print(enchantment_1('Sword'))
    enchantment_2 = enchantment_factory('Frozen')
    print(enchantment_2('Shield'))

    print("\nTesting memory vault...")
    vault = memory_vault()
    store = vault['store']
    recall = vault['recall']

    store('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")


if __name__ == "__main__":
    main()
