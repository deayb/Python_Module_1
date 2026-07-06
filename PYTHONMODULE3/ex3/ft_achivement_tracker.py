#!/usr/bin/env python3

import random

ACHIEVEMENTS = [
    "Crafting Genius", "World Savior", "Master Explorer", "Collector Supreme",
    "Untouchable", "Boss Slayer", "Strategist", "Speed Runner", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind", "Unstoppable",
]


def gen_player_achievements() -> set[str]:
    nb_picks = random.randint(3, len(ACHIEVEMENTS) - 1)
    picks = random.sample(ACHIEVEMENTS, nb_picks)
    return set(picks)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    all_achievements = alice.union(bob, charlie, dylan)
    print(f"All distinct achivements: {all_achievements}\n")

    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achivements: {common}\n")

    only_alice = alice.difference(bob.union(charlie, dylan))
    only_bob = bob.difference(alice.union(charlie, dylan))
    only_charlie = charlie.difference(alice.union(bob, dylan))
    only_dylan = dylan.difference(alice.union(bob, charlie))

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}\n")

    alice_missing = all_achievements.difference(alice)
    bob_missing = all_achievements.difference(bob)
    charlie_missing = all_achievements.difference(charlie)
    dylan_missing = all_achievements.difference(dylan)

    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")
