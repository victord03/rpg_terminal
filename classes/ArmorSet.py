from classes.ArmorPiece import ArmorPiece


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

    def __iter__(self):
        """Iterates only among the different armor pieces (Removes 'name' and 'weight' attributes)."""
        dict_armor_pieces = self.__dict__.copy()
        dict_armor_pieces.pop('name')
        dict_armor_pieces.pop('weight')

        return iter(dict_armor_pieces.items())

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
