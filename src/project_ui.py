from classes.project_class_character import Character
from utils.project_constants import NEW_LINE


def display_combat_options() -> None:

    print(
        NEW_LINE
        + "Next action ?"
        + "\n0: ATTACK\t1: FLEE"
    )


def display_battle_start(char: Character, opp: Character):

    print(
        NEW_LINE
        + f"FIGHT BREAKOUT: {char.name} (LVL {char.level}, {char.hp}/{char.hp_max} HP)"
        + f" VS {opp.name} (LVL {opp.level}, {opp.hp}/{opp.hp_max} HP)"
        + NEW_LINE
    )


def display_battle_recap(defeated_char: Character) -> str:
    return f"{defeated_char.name} has been defeated!"


def display_flee_success() -> str:
    return "Successfully fled combat."


def display_flee_fail() -> str:
    return "Cannot flee!"


def display_xp_awarded(winning_char: Character, defeated_char: Character) -> str:
    return f"{winning_char.name} is awarded {defeated_char.xp_yield} XP."


def display_combatants_health(char: Character, opp: Character):
    print(char)
    print(opp)


def display_level_up(char: Character):
    print(
        f"\n{char.name} leveled up to LVL {char.level}! ({char.show_xp()})"
    )
