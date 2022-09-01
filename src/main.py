import project_ui as ui
from classes.Character import Character
from classes.Map import Map
from data.weapon_data import weapon_data as wd
from utils.constants import DECO
from utils.automation import instantiate_all_weapons as iaw


# todo: remove multiple exit points
def fight(
        char: Character,
        enemy: Character,
        printing=True) -> tuple[Character, int]:

    if printing:
        print(ui.display_battle_start(char, enemy))

    i = 1
    while True:

        if printing:
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

                if printing:
                    print(ui.display_hit(char, enemy))

            case 1:

                code = combat_options[choice](enemy)

                if code == 0:
                    print(ui.display_flee_success())
                    # todo: function exit point 1
                    return char, 0
                elif code == 1:
                    print(ui.display_flee_fail())

        if not enemy.is_alive():

            if printing:
                print(ui.display_battle_recap(enemy))

            # todo: function exit point 2
            return char, enemy.xp_yield

        # todo: implement AI call here (deciding NPC combat actions)
        enemy.attack(char)

        if printing:

            print(ui.display_hit(enemy, char))

            print()

            # todo: replace with print(ui.display_combatants_health(char, enemy)[0], ui.display_combatants_health(char, enemy)[1]) ?
            char_disp, enemy_disp = ui.display_combatants_health(char, enemy)
            print(char_disp)
            print(enemy_disp)

            print()

        if not char.is_alive():

            if printing:
                print(ui.display_battle_recap(char))

            # todo: function exit point 3
            return enemy, char.xp_yield

        i += 1


def main():

    # Weapons
    all_weapons = iaw(wd)

    # Characters
    hero = Character.make_main_hero()
    enemy = Character.make_goblin()

    # Methods
    hero.set_weapon(all_weapons['longsword'])
    enemy.set_weapon(all_weapons['priscilla_dagger'])

    # print(ui.display_both_characters(hero, enemy))

    winner, xp = fight(hero, enemy, printing=True)

    # new_map = Map()

    """for _ in range(4):
        new_map.add_next_room()

    print(new_map.rooms.items())
    print(new_map.rooms["room1"].display_info())"""


if __name__ == "__main__":
    main()
