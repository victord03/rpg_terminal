import logic as lg
from classes.Character import Character
from classes.Map import Map


def main():

    # Weapons
    weapons = lg.weapons

    # Characters
    hero = Character.make_main_hero()
    enemy = Character.make_goblin()

    # Methods
    hero.set_weapon(weapons['bkgs'])
    enemy.set_weapon(weapons['large_club'])

    lg.fight(hero, enemy)

    # MAP
    # new_map = Map()


if __name__ == "__main__":
    main()
