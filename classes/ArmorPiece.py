from utils.constants import NEW_LINE as NL, TAB as T


class APAttributes:
    weight: float
    price: int

    def __init__(self, price: int, weight: float) -> None:
        self.price = price
        self.weight = weight


class APResistances:
    physical: dict
    magical: int
    fire: int
    lightning: int

    def __init__(self, physical: dict, magical: int, fire: int, lightning: int) -> None:
        self.physical = {
            "slash": physical["slash"],
            "strike": physical["strike"],
            "thrust": physical["thrust"],
        }
        self.magical = magical
        self.fire = fire
        self.lightning = lightning

    def __iter__(self):
        return iter(self.__dict__.items())

    def show_resistances(self) -> str:
        """Returns a string with the armor resistances per category."""

        concat = "\nPHYSICAL:"

        for key, res in self:

            if key == "physical":

                for inner_key, each in self.physical.items():
                    concat += f"\n\t{inner_key.upper()} {each}"
            else:
                concat += f"\n{key.upper()}: {res}"

        return concat


class ArmorPiece:
    resistances: APResistances
    attributes: APAttributes

    def __init__(self, data_dict: dict) -> None:

        self.resistances = APResistances(
            data_dict["physical"],
            data_dict["magical"],
            data_dict["fire"],
            data_dict["lightning"],
        )

        self.attributes = APAttributes(data_dict["price"], data_dict["weight"])

    def __iter__(self):
        # todo: forgot to wrap iter()
        return self.__dict__.items()

    def show_details(self) -> str:
        """Returns a string detailing all Resistances and Attribute values set to this instance."""

        slash = self.resistances.physical["slash"]
        strike = self.resistances.physical["strike"]
        thrust = self.resistances.physical["thrust"]

        physical = (
            f"{NL}{T}{T}Physical [Slash: {slash}, Strike: {strike}, Thrust {thrust}]"
        )
        magical = f"{NL}{T}{T}Magical: {self.resistances.magical}"
        fire = f"{NL}{T}{T}Fire: {self.resistances.fire}"
        lightning = f"{NL}{T}{T}Lightning: {self.resistances.lightning}"

        price = f"{NL}{T}{T}Price: {self.attributes.price}"
        weight = f"{NL}{T}{T}Price: {self.attributes.weight}"

        return f"{physical}{magical}{fire}{lightning}{price}{weight}"
