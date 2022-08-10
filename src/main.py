from project_ui import display_level_up, display_battle_start, display_combat_options, display_flee_success, display_flee_fail, display_battle_recap, display_combatants_health
from classes.project_class_character import Character
from classes.project_class_weapon import Weapon
from data.weapon_data import rusty_dagger, black_knight_halberd, unarmed
from data.character_data import goblin, main_char
from utils.project_constants import DECO


def coordinate_combat_phase(
        char: Character,
        enemy: Character,
        printing=True) -> tuple[Character, int]:

    if printing:
        display_battle_start(char, enemy)

    i = 1
    while True:

        if printing:
            print(f"Round {i}")
            print(DECO)

        combat_options = {
            0: char.attack,
            1: char.flee,
        }

        display_combat_options()

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
                    print(display_flee_success())
                    return char, 0
                elif code == 1:
                    print(display_flee_fail())

        if not enemy.is_alive():

            if printing:
                print(display_battle_recap(enemy))

            return char, enemy.xp_yield

        # todo: implement AI call here (deciding NPC combat actions)
        enemy.attack(char)

        if printing:

            print(
                f"{enemy.name} hits {char.name} for {enemy.weapon.damage} damage ({enemy.weapon.name})."
            )

            print()

            display_combatants_health(char, enemy)

            print()

        if not char.is_alive():

            if printing:
                print(display_battle_recap(char))

            return enemy, char.xp_yield

        i += 1


def main():

    # Weapons
    fist = Weapon(unarmed["name"], unarmed["damage"], unarmed["weapon_type"])
    bkh = Weapon(black_knight_halberd["name"], black_knight_halberd["damage"], black_knight_halberd["weapon_type"])
    rd = Weapon(rusty_dagger["name"], rusty_dagger["damage"], rusty_dagger["weapon_type"])

    # Hero
    hero_name = "Sire McDoughNat"
    hero = Character(hero_name, fist, main_char["hp"])
    hero.stats["Speed"] = 2
    hero.equip_weapon(bkh)

    # Enemy
    enemy = Character(goblin["name"], fist, goblin["hp"])
    enemy.set_xp_yield()
    enemy.stats["Speed"] = 1
    enemy.equip_weapon(rd)

    winner, xp = coordinate_combat_phase(hero, enemy, printing=True)

    winner.xp += xp

    if hero.is_ready_to_level_up():
        hero.level_up()
        display_level_up(winner)


    """
    # Value testing
    # b = project_value_testing.check_xp_values(hero, 60)
    # project_value_testing.display_xp_values(b)

    # hero.level = 1

    # print()
    # project_value_testing.check_xp_yield_values(hero, 60, b)
    """


if __name__ == "__main__":
    main()
