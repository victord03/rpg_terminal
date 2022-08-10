
class Weapon:
    name: str
    damage: int
    weapon_type: str

    def __init__(self, name: str, damage: int, weapon_type: str):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type

    def __repr__(self) -> str:
        return f"WEAPON: [{self.name}: {self.weapon_type} CLASS, {self.damage} DMG]"
