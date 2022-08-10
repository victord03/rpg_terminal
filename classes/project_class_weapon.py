
class Weapon:
    name: str
    weapon_type: str
    damage: int

    def __repr__(self) -> str:
        return f"WEAPON: [{self.name}: {self.weapon_type} CLASS, {self.damage} DMG]"
