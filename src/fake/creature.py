from models.creature import Creature

_creatures = [
    Creature(name='Knopa',
             country='RU',
             area='Zapolarnaya',
             descrioption='Very dangerous',
             aka="Mops9ka"),
    Creature(name='Alka',
             country='RU',
             area='Babushkina',
             descrioption='Very small',
             aka="*"),
    Creature(name='yeti',
            country='CN',
            area='Himalayas',
            descrioption='Hirsute Himalayan',
            aka='Abominable Snowman'
            )
]

def get_all() -> list[Creature]:
    'Return all creatures'
    return _creatures

def get_one(name: str) -> Creature | None:
    'Return one creature'
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    'Create creature'
    return creature

def modify(creature: Creature) -> Creature:
    'Modify creature'
    return creature

def replace(creature: Creature) -> Creature:
    'Replace creature'
    return creature

def delete(creature: Creature) -> Creature:
    'Delete creature'
    return creature