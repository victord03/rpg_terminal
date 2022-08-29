from classes.Weapon import Weapon
from data.weapon_data import weapons as wps


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

    def __init__(self, name: str, hp_max: int, stats: list[tuple[str, int]]):
        self.name = name
        self.weapon = Weapon(wps["unarmed"]["pn"], wps["unarmed"]["damage"])
        self.alive = True
        self.hp_max = hp_max
        self.hp = self.hp_max
        self.level = 1
        self.xp = 0
        self.set_xp_bar()
        self.tier = 1
        self.set_xp_yield()
        self.stats = {}

        for tuple_values in stats:
            self.stats[tuple_values[0]] = tuple_values[1]

    @classmethod
    def make_main_hero(cls):

        symbols = ["'", ":", "[", "]", '"', "(", ")", "*", "%", "$", "#", "@", "!", "<", ">", "?", "\\", "/", " "]

        name = "/"
        a = True
        while a:
            for char in symbols:
                if name.count(char) != 0:
                    name = input("\nInsert your character name:\n> ")
                    a = True
                    break
                else:
                    a = False

        hp = 48
        stats = [("Speed", 2)]

        return cls(name, hp, stats)

    @classmethod
    def make_goblin(cls):

        hp = 15
        name = "Goblin"
        stats = [("Speed", 1)]

        return cls(name, hp, stats)

    # DISPLAY METHODS
    def show_self(self) -> str:
        return f"{self.name}:" + " " + self.show_health()

    def show_health(self) -> str:
        return f"{self.hp}/{self.hp_max} HP"

    def show_weapon(self) -> str:
        return f"[Weapon: {self.weapon.name}, {self.weapon.damage} DMG]"

    def show_xp(self) -> str:
        return f"{self.xp}/{self.xp_bar} XP"

    def show_health_and_weapon(self) -> str:
        return self.show_self() + ", " + self.show_weapon()

    # ACTION METHODS
    def equip_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon

    def attack(self, other=None) -> None:
        other.hp -= self.weapon.damage

        if not other.is_alive():
            other.alive = False

    def flee(self, other=None) -> int:

        if self.stats["Speed"] > other.stats["Speed"]:
            return 0
        else:
            return 1

    def level_up(self) -> None:

        print(f"LEVEL: {self.level} XP BAR: {self.xp_bar}")

        while self.xp >= self.xp_bar:

            if self.xp > self.xp_bar:
                self.xp -= self.xp_bar
                self.level += 1
            elif self.xp == self.xp_bar:
                self.xp = 0
                self.level += 1

            self.set_xp_bar()
            print(f"LEVEL: {self.level} XP BAR: {self.xp_bar}")

    # CHECK METHODS
    def is_alive(self) -> bool:
        return self.hp > 0

    def is_ready_to_level_up(self) -> bool:
        return self.xp >= self.xp_bar

    # SET METHODS
    def set_xp_bar(self) -> None:

        padding = 8
        scale = 7

        self.xp_bar = (self.level + padding) * (self.level * scale)

    def set_xp_yield(self) -> None:
        padding = 5
        self.xp_yield = (self.level + padding) * (self.tier * self.level)


