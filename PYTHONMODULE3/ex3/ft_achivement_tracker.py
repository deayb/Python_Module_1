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
    print(f"Player Dylan: {dylan}")






# liste = ["epee", "bouclier", "potion", "casque", "armure", "arc"]
# nb = random.randint(2, 4)
# print(nb)
# picks = random.sample(liste, nb)
# print(picks)
# mon_set = set(picks)
# print(mon_set)