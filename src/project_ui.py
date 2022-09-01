from classes.Character import Character
from utils.constants import NEW_LINE as NL


# GENERAL DISPLAYS
def display_both_characters(char: Character, opp: Character) -> str:

    hnw_1 = f"{NL}{display_char_health_and_weapon(char)}, "
    xp_1 = f"{display_char_xp(char)}. "
    as_1 = f"Wearing the [{display_armor_set(char)}]"
    hnw_2 = f"{NL}{NL}{display_char_health_and_weapon(opp)}, "
    xp_2 = f"{display_char_xp(opp)}. "
    as_2 = f"Wearing the [{display_armor_set(opp)}]"

    return hnw_1 + xp_1 + as_1 + hnw_2 + xp_2 + as_2


# PRE-COMBAT DISPLAYS
def display_battle_start(char: Character, opp: Character) -> str:
    return NL + f"FIGHT BREAKOUT: {display_char_level_and_hp(char)}" + f" VS {display_char_level_and_hp(opp)}" + NL


# IN-COMBAT DISPLAYS
def display_combat_options() -> str:
    return NL + "Next action ?" + "\n0: ATTACK\t1: FLEE"


def display_hit(char: Character, opp: Character) -> str:
    return f"{char.name} hits {opp.name} for {char.weapon.show_damage_total()} damage ({char.weapon.name})."


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


def display_level_up(char: Character) -> str:
    return f"\n{char.name} leveled up to LVL {char.level}! ({display_char_xp(char)})"


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
    return f"{char.name} (LVL {char.level}, {display_char_health(char)})"


def display_char_xp(char: Character) -> str:
    return f"{char.xp}/{char.xp_bar} XP"


def display_armor_set(char: Character) -> str:
    return char.armor.show_self_simple()
