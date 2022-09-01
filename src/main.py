import project_ui as ui
from classes.Character import Character
from classes.Weapon import Weapon
from classes.Map import Map
from data.weapon_data import weapons as wd
from utils.project_constants import DECO


def fight(
        char: Character,
        enemy: Character,
        printing=True) -> tuple[Character, int]:

    if printing:
        ui.display_battle_start(char, enemy)

    i = 1
    while True:

        if printing:
            print(f"Round {i}")
            print(DECO)

        combat_options = {
            0: char.attack,
            1: char.flee,
        }

        ui.display_combat_options()

        choice = int(input("> "))

        combat_options[choice](enemy)

        match choice:

            case 0:

                if printing:
                    print(
                        f"{char.name} hits {enemy.name} for {char.weapon.damage} damage ({char.weapon.name})."
                    )

            case 1:

                code = combat_options[choice](enemy)

                if code == 0:
                    print(ui.display_flee_success())
                    return char, 0
                elif code == 1:
                    print(ui.display_flee_fail())

        if not enemy.is_alive():

            if printing:
                print(ui.display_battle_recap(enemy))

            return char, enemy.xp_yield

        # todo: implement AI call here (deciding NPC combat actions)
        enemy.attack(char)

        if printing:

            print(
                f"{enemy.name} hits {char.name} for {enemy.weapon.damage} damage ({enemy.weapon.name})."
            )

            print()

            char_disp, enemy_disp = ui.display_combatants_health(char, enemy)
            print(char_disp)
            print(enemy_disp)

            print()

        if not char.is_alive():

            if printing:
                print(ui.display_battle_recap(char))

            return enemy, char.xp_yield

        i += 1


def main():

    # Weapons
    rd = Weapon(wd["rusty_dagger"]["pn"], wd["rusty_dagger"]["damage"])
    ss = Weapon(wd["short_sword"]["pn"], wd["short_sword"]["damage"])

    # Characters
    hero = Character.make_main_hero()
    enemy = Character.make_goblin()

    # Methods
    hero.set_weapon(ss)
    enemy.set_weapon(rd)

    """print(
        "\n",
        ui.display_char_health_and_weapon(hero),
        ui.display_char_xp(hero),
        "\n",
        ui.display_char_health_and_weapon(enemy),
        ui.display_char_xp(enemy)
    )"""

    # winner, xp = fight(hero, enemy, printing=True)

    # hero.xp += 4150
    # hero.level_up()
    # ui.display_level_up(hero)

    new_map = Map()

    for _ in range(4):
        new_map.add_next_room()

    print(new_map.rooms.items())
    print(new_map.rooms["room1"].display_info())


if __name__ == "__main__":
    main()
