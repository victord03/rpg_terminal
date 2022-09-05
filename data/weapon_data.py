"""This file holds all weapon and armor data, and is used as a local database.

    "name": {
        "pn": "",
        "type": "",
        "damage": {
            "slash": 0,
            "strike": 0,
            "thrust": 0,
        },
        "requirements": {
            "strength": 0,
            "dexterity": 0,
        },
    },
"""

# pn = printable name
weapon_data = {
    "unarmed": {
        "pn": "Unarmed",
        "type": "Fist",
        "damage": {
            "slash": 0,
            "strike": 50,
            "thrust": 10,
        },
        "requirements": {
            "strength": 0,
            "dexterity": 0,
        },
    },
    "priscilla_dagger": {
        "pn": "Priscilla's Dagger",
        "type": "Dagger",
        "damage": {
            "slash": 70,
            "strike": 0,
            "thrust": 10,
        },
        "requirements": {
            "dexterity": 6,
            "strength": 20,
        },
    },
    "longsword": {
        "pn": "Longsword",
        "type": "Straight Sword",
        "damage": {
            "slash": 50,
            "strike": 0,
            "thrust": 30,
        },
        "requirements": {
            "dexterity": 10,
            "strength": 10,
        },
    },
    "bks": {
        "pn": "Black Knight Sword",
        "type": "Greatsword",
        "damage": {
            "slash": 20,
            "strike": 120,
            "thrust": 80,
        },
        "requirements": {
            "dexterity": 20,
            "strength": 18,
        },
    },
    "bkgs": {
        "pn": "Black Knight Greatsword",
        "type": "Ultra Greatsword",
        "damage": {
            "slash": 0,
            "strike": 160,
            "thrust": 60,
        },
        "requirements": {
            "strength": 32,
            "dexterity": 18,
        },
    },
    "painting_guardian_sword": {
        "pn": "Painting Guardian Sword",
        "type": "Curved Sword",
        "damage": {
            "slash": 76,
            "strike": 0,
            "thrust": 0,
        },
        "requirements": {
            "strength": 7,
            "dexterity": 20,
        },
    },
    "uchi": {
        "pn": "Uchigatana",
        "type": "Katana",
        "damage": {
            "slash": 60,
            "strike": 0,
            "thrust": 30,
        },
        "requirements": {
            "strength": 14,
            "dexterity": 14,
        },
    },
    "marakumo": {
        "pn": "Marakumo",
        "type": "Curved Greatsword",
        "damage": {
            "slash": 113,
            "strike": 0,
            "thrust": 0,
        },
        "requirements": {
            "strength": 28,
            "dexterity": 13,
        },
    },
    "battle_axe": {
        "pn": "Battle Axe",
        "type": "Axe",
        "damage": {
            "slash": 20,
            "strike": 75,
            "thrust": 0,
        },
        "requirements": {
            "strength": 12,
            "dexterity": 8,
        },
    },
    "bkga": {
        "pn": "Black Knight Greataxe",
        "type": "Great axe",
        "damage": {
            "slash": 50,
            "strike": 180,
            "thrust": 0,
        },
        "requirements": {
            "strength": 36,
            "dexterity": 18,
        },
    },
    "mace": {
        "pn": "Mace",
        "type": "Hammer",
        "damage": {
            "slash": 0,
            "strike": 90,
            "thrust": 0,
        },
        "requirements": {
            "strength": 12,
            "dexterity": 0,
        },
    },
    "large_club": {
        "pn": "Large Club",
        "type": "Great Hammer",
        "damage": {
            "slash": 0,
            "strike": 120,
            "thrust": 0,
        },
        "requirements": {
            "strength": 26,
            "dexterity": 0,
        },
    },
    "dark_hand": {
        "pn": "Dark Hand",
        "type": "Fist",
        "damage": {
            "slash": 0,
            "strike": 200,
            "thrust": 0,
        },
        "requirements": {
            "strength": 0,
            "dexterity": 0,
        },
    },
    "silver_knight_spear": {
        "pn": "Silver Knight Spear",
        "type": "Spear",
        "damage": {
            "slash": 0,
            "strike": 0,
            "thrust": 160,
        },
        "requirements": {
            "strength": 16,
            "dexterity": 22,
        },
    },
    "bkh": {
        "pn": "Black Knight Halberd",
        "type": "Halberd",
        "damage": {
            "slash": 245,
            "strike": 0,
            "thrust": 0,
        },
        "requirements": {
            "strength": 32,
            "dexterity": 18,
        },
    },
}
