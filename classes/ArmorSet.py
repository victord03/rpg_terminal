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

        self.weight = self.helmet.attributes.weight + self.body.attributes.weight
        self.weight += self.gauntlet.attributes.weight + self.leggings.attributes.weight

    def show_complete_self(self) -> str:

        # todo: account for missing pieces
        intro = f"{NL}{self.name} Armor Set"
        helmet = f"{NLNLT}HELMET {self.helmet.show_self()}"
        body = f"{NLNLT}BODY {self.body.show_self()}"
        gauntlet = f"{NLNLT}GAUNTLET {self.gauntlet.show_self()}"
        leggings = f"{NLNLT}LEGGINGS {self.leggings.show_self()}"

        return f"{intro}{helmet}{body}{gauntlet}{leggings}"

    def show_self_simple(self) -> str:
        return self.name

    def self_as_dict(self) -> dict:
        return self.__dict__

    def add_all_resistance_values(self) -> dict:

        slash = self.helmet.resistances.physical['slash'] + self.body.resistances.physical['slash']
        slash += self.gauntlet.resistances.physical['slash'] + self.leggings.resistances.physical['slash']

        strike = self.helmet.resistances.physical['strike'] + self.body.resistances.physical['strike']
        strike += self.gauntlet.resistances.physical['strike'] + self.leggings.resistances.physical['strike']

        thrust = self.helmet.resistances.physical['thrust'] + self.body.resistances.physical['thrust']
        thrust += self.gauntlet.resistances.physical['thrust'] + self.leggings.resistances.physical['thrust']

        return {'slash': slash, 'strike': strike, 'thrust': thrust}
