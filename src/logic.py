"""Project logic. Holds all operations that do not belong in classes"""

import project_ui as ui
from classes.Character import Character
from classes.Weapon import Weapon
from utils.constants import DECO
from data.weapon_data import weapon_data as wd


# todo: remove multiple function exit points
# todo: module for more than two participants
def fight(char: Character, enemy: Character):
    """Handles the combat between two characters"""

    print(ui.display_battle_start(char, enemy))

    i = 1
    while True:

        print(f"Round {i}")
        print(DECO)

        combat_options = {
            0: char.attack,
            1: char.flee,
        }

        print(ui.display_combat_options())

        choice = int(input("> "))

        combat_options[choice](enemy)

        match choice:
            case 0:
                print(ui.display_hit(char, enemy))

            case 1:
                code = combat_options[choice](enemy)

                if code == 0:
                    print(ui.display_flee_success())
                    # function exit point 1
                    return char, 0
                # changed below elif statement to if following pylint advice. Test functionality.
                if code == 1:
                    print(ui.display_flee_fail())

        if not enemy.is_alive():

            print(ui.display_battle_recap(enemy))

            # function exit point 2
            return "Not implemented yet"

        enemy.attack(char)

        print(ui.display_hit(enemy, char))

        print()

        char_disp, enemy_disp = ui.display_combatants_health(char, enemy)
        print(char_disp)
        print(enemy_disp)

        print()

        if not char.is_alive():

            print(ui.display_battle_recap(char))

            # function exit point 3
            return "Not implemented yet"

        i += 1


def instantiate_all_weapons(weapon_data: dict):
    """Instantiates all weapons in the weapon_data dictionary."""

    weapons_dict = {}

    for key, value in weapon_data.items():
        weapons_dict[key] = Weapon(
            name=value["pn"],
            damage=value["damage"],
            weapon_type=value["type"],
            requirements=value["requirements"],
        )

    return weapons_dict


weapons = instantiate_all_weapons(wd)
