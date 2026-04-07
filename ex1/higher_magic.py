from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: (
        spell(target, power) if condition(target, power) else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [spell(target, power) for spell in spells]


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 50)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")

    def power_check(target: str, power: int) -> str:
        return str(power)

    amplified = power_amplifier(power_check, 3)
    print(f"Original: 10, Amplified: {amplified('Any', 10)}")

    print("\nTesting conditional caster...")

    conditional = conditional_caster(lambda t, p: p >= 20, fireball)
    print(f"Power 30: {conditional('Orc', 30)}")
    print(f"Power 10: {conditional('Orc', 10)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, fireball])
    seq_result = sequence("Goblin", 15)
    print(f"Sequence results: {seq_result}")
