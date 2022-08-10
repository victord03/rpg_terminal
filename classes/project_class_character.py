from classes.project_class_weapon import Weapon


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

    def __init__(self, name: str, weapon: Weapon, hp_max: int):
        self.name = name
        self.alive = True
        self.hp_max = hp_max
        self.hp = self.hp_max
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

    def show_xp(self) -> str:
        return f"{self.xp}/{self.xp_bar} XP"

    def show_health_and_weapon(self) -> str:
        return self.__repr__() + ", " + self.show_weapon()

    # ACTION METHODS
    def equip_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon

    def attack(self, other: any) -> None:
        other.hp -= self.weapon.damage

        if not other.is_alive():
            other.alive = False

    def flee(self, other: any) -> int:

        if self.stats["Speed"] > other.stats["Speed"]:
            return 0
        else:
            return 1

    def level_up(self) -> None:

        if self.xp > self.xp_bar:
            self.xp -= self.xp_bar
            self.level += 1

        elif self.xp == self.xp_bar:
            self.xp = 0
            self.level += 1

    # CHECK METHODS
    def is_alive(self) -> bool:
        return self.hp > 0

    def is_ready_to_level_up(self) -> bool:
        return self.xp >= self.xp_bar

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


