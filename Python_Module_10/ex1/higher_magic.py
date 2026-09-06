from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def power_amplifier(base_spell: Callable, multipler: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multipler)
    return amplified


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return spell1(target, power), spell2(target, power)
    return combined


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def casted(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return casted


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        result = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return sequence


def main() -> None:

    print("\nTesting spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    hit, healer = combined_spell("Dragon", 20)
    print(f"Combined spell result: {hit}, {healer}\n")

    print("Testing power amplified...")
    mega = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega('Dragon', 10)}")

    # print("\nTesting conditional caster...")
    # cond = conditional_caster(lambda t, p: p >= 50, fireball)
    # print(cond("Dragon", 80))
    # print(cond("Dragon", 10))

    # print("\nTesting spell sequence...")
    # combo = spell_sequence([fireball, heal])
    # for result in combo("Dragon", 20):
    #     print(result)


if __name__ == "__main__":
    main()
