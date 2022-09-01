"""This file will hold all weapon data as a local database"""

# document template "": {"pn": "", "damage": 0},

# pn = printable name
weapons = {

    "unarmed": {
        "pn": "Unarmed", "damage": 1
    },

    "rusty_dagger": {
        "pn": "Rusty Dagger", "damage": 2
    },

    "short_sword": {
        "pn": "Short Sword", "damage": 3
    },

    "long_sword": {
        "pn": "Long Sword", "damage": 4
    },

    "black_knight_halberd": {
        "pn": "Black Knight Halberd", "damage": 7
    },
}

weapons_2 = {

    "unarmed": {
        "pn": "Unarmed",
        "type": "Fist",
        "damage": 10,
        "requirements": {
            "strength": 0,
            "dexterity": 0,
        },
    },

    "priscilla_dagger": {
        "pn": "Priscilla's Dagger",
        "type": "Dagger",
        "damage": 120,
        "requirements": {
            "dexterity": 6,
            "strength": 20,
        },
    },

    "longsword": {
        "pn": "Longsword",
        "type": "Straight Sword",
        "damage": 200,
        "requirements": {
            "dexterity": 10,
            "strength": 10,
        },
    },

    "bks": {
        "pn": "Black Knight Sword",
        "type": "Greatsword",
        "damage": 330,
        "requirements": {
            "dexterity": 20,
            "strength": 18,
        },
    },

    "bkgs": {
        "pn": "Black Knight Greatsword",
        "type": "Ultra Greatsword",
        "damage": 330,
        "requirements": {
            "strength": 32,
            "dexterity": 18,
        },
    },

    "painting_guardian_sword": {
        "pn": "Painting Guardian Sword",
        "type": "Curved Sword",
        "damage": 190,
        "requirements": {
            "strength": 7,
            "dexterity": 20,
        },
    },

    "uchi": {
        "pn": "Uchigatana",
        "type": "Katana",
        "damage": 225,
        "requirements": {
            "strength": 14,
            "dexterity": 14,
        },
    },

    "marakumo": {
        "pn": "Marakumo",
        "type": "Curved Greatsword",
        "damage": 282,
        "requirements": {
            "strength": 28,
            "dexterity": 13,
        },
    },

    "battle_axe": {
        "pn": "Battle Axe",
        "type": "Axe",
        "damage": 237,
        "requirements": {
            "strength": 12,
            "dexterity": 8,
        },
    },

    "bkga": {
        "pn": "Black Knight Greataxe",
        "type": "Great axe",
        "damage": 343,
        "requirements": {
            "strength": 36,
            "dexterity": 18,
        },
    },

    "mace": {
        "pn": "Mace",
        "type": "Hammer",
        "damage": 227,
        "requirements": {
            "strength": 12,
            "dexterity": 0,
        },
    },

    "large_club": {
        "pn": "Large Club",
        "type": "Great Hammer",
        "damage": 300,
        "requirements": {
            "strength": 26,
            "dexterity": 0,
        },
    },

    "dark_hand": {
        "pn": "Dark Hand",
        "type": "Fist",
        "damage": 200,
        "requirements": {
            "strength": 0,
            "dexterity": 0,
        },
    },

    "silver_knight_spear": {
        "pn": "Silver Knight Spear",
        "type": "Spear",
        "damage": 244,
        "requirements": {
            "strength": 16,
            "dexterity": 22,
        },
    },

    "bkh": {
        "pn": "Black Knight Halberd",
        "type": "Halberd",
        "damage": 367,
        "requirements": {
            "strength": 32,
            "dexterity": 18,
        },
    },
}
