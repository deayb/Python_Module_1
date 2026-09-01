#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    challenger1 = factory1.create_base()
    print(challenger1.describe())
    print(" vs.")
    challenger2 = factory2.create_base()
    print(challenger2.describe())
    print(" fight!")
    print(challenger1.attack())
    print(challenger2.attack())


if __name__ == "__main__":
    fire_factory = FlameFactory()
    water_factory = AquaFactory()

    test_factory(fire_factory)
    print()
    test_factory(water_factory)
    print()
    battle(fire_factory, water_factory)
