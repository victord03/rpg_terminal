
class Weapon:
    name: str
    weapon_type: str
    damage: int

    def __repr__(self) -> str:
        return f"WEAPON: [{self.name}: {self.weapon_type} CLASS, {self.damage} DMG]"


class Character:

    name: str

    hp: int
    hp_max: int

    alive: bool

    weapon: Weapon

    level: int

    xp: int
    xp_bar: int
    xp_yield: int

    tier: int

    stats: dict

    def __init__(self, name: str, weapon: Weapon):
        self.name = name
        self.alive = True
        self.level = 1
        self.xp = 0
        self.set_xp_bar()
        self.xp_yield = 1
        self.tier = 1
        self.stats = {}
        self.equip_weapon(weapon)

    # DISPLAY METHODS
    def __repr__(self) -> str:
        return f"{self.name}:" + " " + self.show_health()

    def show_health(self) -> str:
        return f"{self.hp}/{self.hp_max} HP"

    def show_weapon(self) -> str:
        return f"[Weapon: {self.weapon.name}, {self.weapon.damage} DMG]"

    def show_health_and_weapon(self) -> str:
        return self.__repr__() + ", " + self.show_weapon()

    # ACTION METHODS
    def equip_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon

    def attack(self, other: any) -> None:
        other.hp -= self.weapon.damage

        if not other.is_alive():
            other.alive = False

    def flee(self, other: any) -> tuple:

        if self.stats["Speed"] > other.stats["Speed"]:
            return "Fled combat.", 0
        else:
            return "Cannot run away!", 1

    def level_up(self) -> None:

        if self.xp > self.xp_bar:
            self.xp -= self.xp_bar
            self.level += 1

        elif self.xp == self.xp_bar:
            self.xp = 0
            self.level += 1

    def award_xp(self) -> int:
        return self.xp_yield

    # CHECK METHODS
    def is_alive(self) -> bool:
        return self.hp > 0

    def is_ready_to_level_up(self) -> tuple[bool, str]:
        return self.xp >= self.xp_bar, f"{self.name}: {self.xp}/{self.xp_bar} XP"

    # SET METHODS
    def set_xp_bar(self) -> None:

        """
        padding: 8; scale: 7

        Level 1: 63 EXP
        Level 2: 140 EXP
        Level 3: 231 EXP
        Level 4: 336 EXP
        Level 5: 455 EXP
        Level 6: 588 EXP
        Level 7: 735 EXP
        Level 8: 896 EXP
        Level 9: 1071 EXP
        Level 10: 1260 EXP
        """

        padding = 8
        scale = 7

        self.xp_bar = (self.level + padding) * (self.level * scale)

    def set_xp_yield(self) -> None:
        padding = 5
        self.xp_yield = (self.level + padding) * (self.tier * self.level)


