from models.explorer import Explorer

_explorers = [
    Explorer(name='Dimasik Evstigneev',
             country='RU',
             description="Very cool boy"),
    Explorer(name='Irisa Pereguda',
             country='FR',
             description='So sexy girl.')
]

def get_all() -> list[Explorer]:
    'Return all explorers'
    return _explorers

def get_one(name: str) -> Explorer | None:
    'Return one explorer'
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create(explorer: Explorer) -> Explorer:
    'Create explorer'
    return explorer

def modify(explorer: Explorer) -> Explorer:
    'Modify explorer'
    return explorer

def replace(explorer: Explorer) -> Explorer:
    'Replace explorer'
    return explorer

def delete(explorer: Explorer) -> Explorer:
    'Delete explorer'
    return explorer