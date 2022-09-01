from classes.Weapon import Weapon


def instantiate_all_weapons(weapon_data: dict):

    weapons = {}

    for key, value in weapon_data.items():
        weapons[key] = Weapon(
            name=value['pn'],
            damage=value['damage'],
            weapon_type=value['type'],
            requirements=value['requirements']
        )

    return weapons
