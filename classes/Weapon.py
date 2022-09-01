
class Weapon:
    name: str
    weapon_type: str
    damage: dict
    requirements: dict

    def __init__(self, name: str, damage: dict, weapon_type: str, requirements: dict):
        self.name = name
        self.damage = {
            'slash': damage['slash'],
            'strike': damage['strike'],
            'thrust': damage['thrust']
        }
        self.weapon_type = weapon_type
        self.requirements = requirements

    def show_complete_self(self) -> str:
        name = self.name
        damage = f"(SLASH: {self.damage['slash']}, STRIKE: {self.damage['strike']}, THRUST: {self.damage['thrust']})"
        weapon_type = f"TYPE: {self.weapon_type}"
        req_str = f"REQ STR: {self.requirements['str']}"
        req_dex = f"REQ DEX: {self.requirements['dex']}"
        return f"WEAPON ({name} [DAMAGE: {damage}, {weapon_type}, {req_str}, {req_dex}])"

    def show_damage_total(self) -> str:
        damage = self.damage['slash'] + self.damage['strike'] + self.damage['thrust']
        return str(damage)
