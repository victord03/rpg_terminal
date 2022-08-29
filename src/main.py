import project_ui as ui
from classes.Character import Character
from classes.Weapon import Weapon
from data.weapon_data import weapons as wps
from utils.project_constants import DECO


def coordinate_combat_phase(
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
    # bkh = Weapon(wps["black_knight_halberd"]["pn"], wps["black_knight_halberd"]["damage"])
    rd = Weapon(wps["rusty_dagger"]["pn"], wps["rusty_dagger"]["damage"])
    ss = Weapon(wps["short_sword"]["pn"], wps["short_sword"]["damage"])

    # Characters
    hero = Character.make_main_hero()
    enemy = Character.make_goblin()

    # Methods
    hero.equip_weapon(ss)
    enemy.equip_weapon(rd)

    print(
        "\n",
        ui.display_char_health_and_weapon(hero),
        ui.display_char_xp(hero),
        "\n",
        ui.display_char_health_and_weapon(enemy),
        ui.display_char_xp(enemy)
    )

    # winner, xp = coordinate_combat_phase(hero, enemy, printing=True)

    # hero.xp += 4150
    # hero.level_up()
    # ui.display_level_up(hero)


if __name__ == "__main__":
    main()
