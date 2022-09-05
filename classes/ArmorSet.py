from classes.ArmorPiece import ArmorPiece
from utils.constants import NLNLT, NEW_LINE as NL


class ArmorSet:
    name: str
    helmet: ArmorPiece
    body: ArmorPiece
    gauntlet: ArmorPiece
    leggings: ArmorPiece
    weight: float

    def __init__(self, data_dict: dict) -> None:
        self.name = data_dict["pn"]
        self.helmet = ArmorPiece(data_dict["helmet"])
        self.body = ArmorPiece(data_dict["body"])
        self.gauntlet = ArmorPiece(data_dict["gauntlet"])
        self.leggings = ArmorPiece(data_dict["leggings"])

        self.weight = int()

        for key, armor_piece in self:
            self.weight += armor_piece.attributes.weight

        # self.weight = self.helmet.attributes.weight + self.body.attributes.weight
        # self.weight += self.gauntlet.attributes.weight + self.leggings.attributes.weight

    def __iter__(self):
        """Iterates only among the different armor pieces (Removes 'name' and 'weight' attributes)."""
        dict_armor_pieces = self.__dict__.copy()
        dict_armor_pieces.pop('name')
        dict_armor_pieces.pop('weight')

        return iter(dict_armor_pieces.items())

    def show_complete_self(self) -> str:
        """Displays all current armor stats"""

        # todo: account for missing pieces
        intro = f"{NL}{self.name} Armor Set"
        helmet = f"{NLNLT}HELMET {self.helmet.show_self()}"
        body = f"{NLNLT}BODY {self.body.show_self()}"
        gauntlet = f"{NLNLT}GAUNTLET {self.gauntlet.show_self()}"
        leggings = f"{NLNLT}LEGGINGS {self.leggings.show_self()}"

        return f"{intro}{helmet}{body}{gauntlet}{leggings}"

    def show_armor_name(self) -> str:
        """Returns the name of the armor set."""
        return self.name

    def add_all_resistance_values(self) -> dict:
        """Adds up all resistance values per category, for all armor pieces and returns them into a dict."""

        damage_types = {
            'slash': int(),
            'strike': int(),
            'thrust': int()
        }

        for key, armor_piece in self:

            for damage_type, value in damage_types.items():
                damage_types[damage_type] += armor_piece.resistances.physical[damage_type]

        return damage_types
