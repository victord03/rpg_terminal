import project_classes

NEW_LINE = "\n"
INPUT_DECO = "\n> "
DECO = "-" * 45


# COMBAT FUNCTION
def coordinate_combat_phase(
        char: project_classes.Character,
        enemy: project_classes.Character,
        printing=True) -> tuple[project_classes.Character, int]:

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

                text = combat_options[choice](enemy)[0]
                code = combat_options[choice](enemy)[1]

                print(NEW_LINE + text)

                if code == 0:
                    # todo: implement flee success
                    ...

        if not enemy.is_alive():

            if printing:
                print(display_battle_recap(enemy))

            return char, enemy.award_xp()

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

            return enemy, char.award_xp()

        i += 1


# PRINTING FUNCTIONS
def display_combat_options() -> None:

    print(
        NEW_LINE
        + "Next action ?"
        + "\n0: ATTACK\t1: FLEE"
    )


def display_battle_start(char: project_classes.Character, opp: project_classes.Character):

    print(
        NEW_LINE
        + f"FIGHT BREAKOUT: {char.name} (LVL {char.level}, {char.hp}/{char.hp_max} HP)"
        + f" VS {opp.name} (LVL {opp.level}, {opp.hp}/{opp.hp_max} HP)"
        + NEW_LINE
    )


def display_battle_recap(defeated_char: project_classes.Character) -> str:
    return f"{defeated_char.name} has been defeated!"


def display_xp_awarded(winning_char: project_classes.Character, defeated_char: project_classes.Character) -> str:
    return f"{winning_char.name} is awarded {defeated_char.award_xp()} XP."


def display_combatants_health(char: project_classes.Character, opp: project_classes.Character):
    print(char)
    print(opp)


# VALUE TESTING FUNCTIONS
def check_xp_values(char: project_classes.Character, number_of_levels: int) -> dict:

    dict_of_values = {}

    i = 1
    for level in range(1, number_of_levels + 1):

        char.set_xp_bar()
        xp_needed_to_next_level = char.xp_bar

        dict_of_values[i] = char.xp_bar

        char.xp += xp_needed_to_next_level

        if char.is_ready_to_level_up():
            char.level_up()

        i += 1

    return dict_of_values


def display_xp_values(values_dict: dict):

    for key, value in values_dict.items():
        print(
            f"Level {key}: {value} EXP"
        )


def check_xp_yield_values(char: project_classes.Character, number_of_levels: int, level_dict=None):

    for level in range(1, number_of_levels+1):

        if type(level_dict) == dict:
            print(
                f"Level: {level} (XP needed for next level: {list(level_dict.values())[level - 1]})"
            )
        else:
            print(
                f"Level: {level}"
            )

        for tier in range(1, 4):

            char.tier = tier

            char.set_xp_yield()

            print(
                f"\tTier {tier}: {char.xp_yield}"
            )

        char.level += 1


# MATH FUNCTION
def calc_percentage(a, b) -> float:
    return round((a / b) * 100, 2)


def main():

    # Weapons
    unarmed = project_classes.Weapon()
    unarmed.name = "Unarmed"
    unarmed.weapon_type = "Regular"
    unarmed.damage = 1

    bkh = project_classes.Weapon()
    bkh.name = "Black Knight Halberd"
    bkh.weapon_type = "Special"
    bkh.damage = 7

    rd = project_classes.Weapon()
    rd.name = "Rusty Dagger"
    rd.weapon_type = "Regular"
    rd.damage = 3

    # Hero
    hero_name = "Sire McDoughNat"
    hero = project_classes.Character(hero_name, unarmed)
    hero.hp = 48
    hero.hp_max = 48
    hero.stats["Speed"] = 2

    # Enemy
    enemy_name = "Goblin"
    goblin = project_classes.Character(enemy_name, unarmed)
    goblin.hp = 15
    goblin.hp_max = 15
    goblin.set_xp_yield()
    goblin.stats["Speed"] = 1

    hero.equip_weapon(bkh)
    goblin.equip_weapon(rd)

    winner, xp = coordinate_combat_phase(hero, goblin, printing=False)

    winner.xp += 64

    check_level_up = False
    if check_level_up:
        print(f"\n{hero.name} is ready to level up ?", hero.is_ready_to_level_up())

        if hero.is_ready_to_level_up():
            hero.level_up()
            print(f"\n{hero.name} (LVL {hero.level}, {hero.xp}/{hero.xp_bar} XP)")

    # Value testing
    # b = check_xp_values(hero, 60)
    # display_xp_values(b)

    # hero.level = 1

    # print()
    # check_xp_yield_values(hero, 60, b)



if __name__ == "__main__":
    main()
