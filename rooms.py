rooms = {
    "hall": {
        "desc": "You are in a dusty hall. A door leads north, a staircase goes down.",
        "exits": {"north": "library", "down": "cellar", "west": "kitchen"},
        "items": ["lamp"],
    },
    "library": {
        "desc": "Shelves full of old books. Something glints on the desk.",
        "exits": {"south": "hall"},
        "items": ["key"],
    },
    "cellar": {
        "desc": "It is pitch black. You hear dripping water.",
        "exits": {"up": "hall", "east": "vault"},
        "items": [],
        "dark": True,
    },
    "kitchen": {
        "desc": "A cold kitchen. It smells like old bread.",
        "exits": {"east": "hall"},
        "items": ["bread"],
    },
    "vault": {
        "desc": "A heavy locked door. This must be the way out!",
        "exits": {"west": "cellar"},
        "items": [],
        "locked": True,
    },
}
