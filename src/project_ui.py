from classes.Character import Character
from utils.project_constants import NEW_LINE


# PRE-COMBAT DISPLAYS
def display_battle_start(char: Character, opp: Character):

    print(
        NEW_LINE
        + f"FIGHT BREAKOUT: {display_char_level_and_hp(char)}"
        + f" VS {display_char_level_and_hp(opp)}"
        + NEW_LINE
    )


# IN-COMBAT DISPLAYS
def display_combat_options() -> None:

    print(
        NEW_LINE
        + "Next action ?"
        + "\n0: ATTACK\t1: FLEE"
    )


def display_combatants_health(char: Character, opp: Character) -> tuple[str, str]:
    return display_char(char), display_char(opp)


# POST-COMBAT DISPLAYS
def display_battle_recap(defeated_char: Character) -> str:
    return f"{defeated_char.name} has been defeated!"


# BATTLE FLEE SUCCESS / FAIL MESSAGES
def display_flee_success() -> str:
    return "Successfully fled combat."


def display_flee_fail() -> str:
    return "Cannot flee!"


# XP & LEVEL UP DISPLAYS
def display_xp_awarded(winning_char: Character, defeated_char: Character) -> str:
    return f"{winning_char.name} is awarded {defeated_char.xp_yield} XP."


def display_level_up(char: Character):
    print(
        f"\n{char.name} leveled up to LVL {char.level}! ({display_char_xp(char)})"
    )


# CLASS DISPLAYS
def display_char(char: Character) -> str:
    return f"{char.name}:" + " " + display_char_health(char)


def display_char_health(char: Character) -> str:
    return f"{char.hp}/{char.hp_max} HP"


def display_char_weapon(char: Character) -> str:
    return f"[Weapon: {char.weapon.name}, {char.weapon.damage} DMG]"


def display_char_health_and_weapon(char: Character) -> str:
    return display_char(char) + ", " + display_char_weapon(char)


def display_char_level_and_hp(char: Character) -> str:
    return f"{char.name} (LVL {char.level}, {char.hp}/{char.hp_max}HP)"


def display_char_xp(char: Character) -> str:
    return f"{char.xp}/{char.xp_bar} XP"

