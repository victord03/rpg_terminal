import logic as lg
from classes.Character import Character
from classes.Map import Map


# check remote branch origin/restructure/classmethod (still exists but cannot be found on github.com)
def main():
    """ Runs the project """

    # Weapons
    weapons = lg.weapons

    # Characters
    hero = Character.make_main_hero()
    hero.set_weapon(weapons['bkgs'])

    enemy = Character.make_goblin()
    enemy.set_weapon(weapons['large_club'])

    # Logic
    lg.fight(hero, enemy)

    # Map
    new_map = Map()


if __name__ == "__main__":
    main()
