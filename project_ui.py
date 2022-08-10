import project_classes

NEW_LINE = "\n"


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
