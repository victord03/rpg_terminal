"""Project UI file. Holds all display methods."""

from classes.Character import Character
from classes.ArmorSet import ArmorSet
from utils.constants import NEW_LINE as NL, NLNLT


# GENERAL DISPLAYS
def display_both_characters(char: Character, opp: Character) -> str:
    """For each of the two characters, displays health, weapon and xp."""

    hnw_1 = f"{NL}{display_char_health_and_weapon(char)}, "
    xp_1 = f"{display_char_xp(char)}. "
    as_1 = f"Wearing the [{display_armor_set_name(char)}]"
    hnw_2 = f"{NL}{NL}{display_char_health_and_weapon(opp)}, "
    xp_2 = f"{display_char_xp(opp)}. "
    as_2 = f"Wearing the [{display_armor_set_name(opp)}]"

    return hnw_1 + xp_1 + as_1 + hnw_2 + xp_2 + as_2


# PRE-COMBAT DISPLAYS
def display_battle_start(char: Character, opp: Character) -> str:
    """Returns a string with the battle start recap message including Characters,
    hp and levels of fighters."""
    char_1 = f"{display_char_level_and_hp(char)}"
    opp_1 = f"{display_char_level_and_hp(opp)}"
    return NL + f"FIGHT BREAKOUT: {char_1}" + f" VS {opp_1}" + NL


# IN-COMBAT DISPLAYS
def display_combat_options() -> str:
    """Returns a string to display all combat options for player turn."""
    return NL + "Next action ?" + "\n0: ATTACK\t1: FLEE"


# todo: needs total rework
def display_hit(char: Character, opp: Character) -> str:
    """Returns a string to display"""
    # todo: need to check for each weapon which damage types are assigned,
    # todo: then compare accordingly with the armor
    who_hits = f"{char.name} hits {opp.name}"
    wpn_dmg = f"{char.weapon.show_damage_total()} damage ({char.weapon.name})"

    # resistances = str(sum([x for key, x in char.armor.add_all_resistance_values().items()]))
    # agn_armor = resistances

    return who_hits + " for " + wpn_dmg + "."


def display_combatants_health(char: Character, opp: Character) -> tuple[str, str]:
    """Returns a string holding combatants name and health values"""
    return display_char_name_and_health(char), display_char_name_and_health(opp)


# POST-COMBAT DISPLAYS
def display_battle_recap(defeated_char: Character) -> str:
    """Returns a string containing the defeated Character name."""
    return f"{defeated_char.name} has been defeated!"


# BATTLE FLEE SUCCESS / FAIL MESSAGES
def display_flee_success() -> str:
    """Returns a string with the successful combat flee message."""
    return "Successfully fled combat."


def display_flee_fail() -> str:
    """Returns a string with the failed combat flee message."""
    return "Cannot flee!"


# XP & LEVEL UP DISPLAYS
def display_xp_awarded(winning_char: Character, defeated_char: Character) -> str:
    """Returns a string with the Character name and the
    xp points won for defeating the given opponent."""
    return f"{winning_char.name} is awarded {defeated_char.xp_yield} XP."


def display_level_up(char: Character) -> str:
    """Returns a string to recap the level up. Contains the
    character name, the new level and the new XP value."""
    return f"\n{char.name} leveled up to LVL {char.level}! ({display_char_xp(char)})"


# CLASS CHARACTER DISPLAYS
def display_char_name_and_health(char: Character) -> str:
    """Returns a string to display the character name and health."""
    return f"{char.name}: " + f"{char.hp}/{char.hp_max} HP"


def display_char_health_and_weapon(char: Character) -> str:
    """Returns a string to display the character name and their
    currently equipped weapon's basic stats."""

    char_name_n_hp = display_char_name_and_health(char)
    comma_space = ", "
    weapon = f"[Weapon: {char.weapon.name} {char.weapon.show_damage_total()} DMG]"

    return char_name_n_hp + comma_space + weapon


def display_char_level_and_hp(char: Character) -> str:
    """Returns a string to display Character name, level and health"""
    # todo: char.name is displayed twice. Fix.
    return f"{char.name} (LVL {char.level}, {display_char_name_and_health(char)})"


def display_char_xp(char: Character) -> str:
    """Returns a string to display the characters current XP value."""
    return f"{char.xp}/{char.xp_bar} XP"


def display_armor_set_name(char: Character) -> str:
    """Returns a string to display the characters current Armor Set name."""
    return char.armor.name


# CLASS ARMOR SET DISPLAYS
def display_armor_set_details(armor_set: ArmorSet) -> str:
    """Returns all the details about each piece of the given armor set"""

    # todo: account for missing pieces
    intro = f"{NL}{armor_set.name} Armor Set"
    helmet = f"{NLNLT}HELMET {armor_set.helmet.show_details()}"
    body = f"{NLNLT}BODY {armor_set.body.show_details()}"
    gauntlet = f"{NLNLT}GAUNTLET {armor_set.gauntlet.show_details()}"
    leggings = f"{NLNLT}LEGGINGS {armor_set.leggings.show_details()}"

    return f"{intro}{helmet}{body}{gauntlet}{leggings}"


def show_armor_name(armor_set: ArmorSet) -> str:
    """Returns the name of the armor set."""
    return armor_set.name
