from classes.Weapon import Weapon
from classes.ArmorSet import ArmorSet


class Character:

    name: str

    hp: int
    hp_max: int

    alive: bool

    weapon: Weapon

    armor: ArmorSet

    level: int

    xp: int
    xp_bar: int
    xp_yield: int

    tier: int

    stats: dict

    def __init__(self, name: str, hp_max: int, stats: list[tuple[str, int]], armor_set: ArmorSet):

        unarmed = {
            "name": "Unarmed",
            "damage": {
                    'slash': 0,
                    'strike': 50,
                    'thrust': 0,
                    },
            "weapon_type": "Fist",
            "requirements": {
                'str': 0,
                'dex': 0
            }
        }

        self.name = name

        self.weapon = Weapon(
            name=unarmed["name"],
            damage=unarmed["damage"],
            weapon_type=unarmed["weapon_type"],
            requirements=unarmed["requirements"]
        )

        self.armor = armor_set

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

        knight_set = {

            "pn": "Knight Set",

            "helmet": {
                "physical": {
                    "slash": 13,
                    "strike": 16,
                    "thrust": 14,
                },
                "magical": 8,
                "fire": 9,
                "lightning": 5,
                "price": 0,
                "weight": 4.2,
            },

            "body": {
                "physical": {
                    "slash": 35,
                    "strike": 43,
                    "thrust": 36,
                },
                "magical": 22,
                "fire": 25,
                "lightning": 13,
                "price": 0,
                "weight": 10.9,
            },

            "gauntlet": {
                "physical": {
                    "slash": 16,
                    "strike": 20,
                    "thrust": 17,
                },
                "magical": 7,
                "fire": 8,
                "lightning": 4,
                "price": 0,
                "weight": 3.5,
            },

            "leggings": {
                "physical": {
                    "slash": 21,
                    "strike": 25,
                    "thrust": 22,
                },
                "magical": 13,
                "fire": 14,
                "lightning": 8,
                "price": 0,
                "weight": 6.4,
            }
        }

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

        hp = 500
        stats = [("Speed", 2)]

        armor_set = ArmorSet(knight_set)

        return cls(name, hp, stats, armor_set)

    @classmethod
    def make_goblin(cls):

        hollow_solder_armor = {

            "pn": "Hollow Soldier Helm",

            "helmet": {
                "physical": {
                    "slash": 10,
                    "strike": 11,
                    "thrust": 9,
                },
                "magical": 6,
                "fire": 6,
                "lightning": 4,
                "price": 0,
                "weight": 3,
            },

            "body": {
                "physical": {
                    "slash": 26,
                    "strike": 29,
                    "thrust": 23,
                },
                "magical": 16,
                "fire": 17,
                "lightning": 10,
                "price": 0,
                "weight": 7.8,
            },

            "gauntlet": {
                "physical": {
                    "slash": 0,
                    "strike": 0,
                    "thrust": 0,
                },
                "magical": 0,
                "fire": 0,
                "lightning": 0,
                "price": 0,
                "weight": 0,
            },

            "leggings": {
                "physical": {
                    "slash": 13,
                    "strike": 14,
                    "thrust": 11,
                },
                "magical": 8,
                "fire": 8,
                "lightning": 6,
                "price": 0,
                "weight": 1.5,
            }
        }

        hp = 500
        name = "Goblin"
        stats = [("Speed", 1)]

        armor_set = ArmorSet(hollow_solder_armor)
        # armor_set.gauntlet = None

        return cls(name, hp, stats, armor_set)

    # ACTION METHODS
    # todo: to test if correct
    def attack(self, other) -> None:

        total_resistances = other.armor.add_all_resistance_values()
        slash_damage = self.weapon.damage['slash'] - total_resistances['slash']
        strike_damage = self.weapon.damage['strike'] - total_resistances['strike']
        thrust_damage = self.weapon.damage['thrust'] - total_resistances['thrust']

        # todo: fix negative values adding health instead of subtracting
        other.hp -= abs(slash_damage + strike_damage + thrust_damage)

        if not other.is_alive():
            other.alive = False

    def flee(self, other) -> int:

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
    def set_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon

    def set_xp_bar(self) -> None:

        padding = 8
        scale = 7

        self.xp_bar = (self.level + padding) * (self.level * scale)

    def set_xp_yield(self) -> None:
        padding = 5
        self.xp_yield = (self.level + padding) * (self.tier * self.level)
