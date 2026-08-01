#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory

def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())

def test_transform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base_t = factory.create_base()
    print(base_t.describe())
    print(base_t.attack())
    print(base_t.transform())
    print(base_t.attack())
    print(base_t.revert())
    print(" evolved:")
    evolved_t = factory.create_evolved()
    print(evolved_t.describe())
    print(evolved_t.attack())
    print(evolved_t.transform())
    print(evolved_t.attack())
    print(evolved_t.revert())

if __name__ == "__main__":
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing(heal_factory)
    print()
    test_transform(transform_factory)
