
class Weapon:
    name: str
    damage: int

    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def show_self(self) -> str:
        return f"WEAPON: [{self.name}: {self.damage} DMG]"
