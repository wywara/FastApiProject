from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str
    area: str
    descrioption: str
    aka: str