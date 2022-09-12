"""Main project file."""

import logic as lg
from classes.Character import Character
from classes.Map import Map


def main():
    """Runs the project"""

    # Weapons
    weapons = lg.weapons

    # Characters
    hero = Character.make_main_hero()
    hero.set_weapon(weapons["bkgs"])

    enemy = Character.make_goblin()
    enemy.set_weapon(weapons["large_club"])

    # Logic
    lg.fight(hero, enemy)

    # Map
    new_map = Map()
    isinstance(new_map, Map)


if __name__ == "__main__":
    main()
