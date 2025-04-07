from service import creature as code
from models.creature import Creature

sample = Creature(name='yeti',
                  country='CN',
                  area='Himalayas',
                  descrioption='Hirsute Himalayan',
                  aka='Abominable Snowman',
                  )

def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exist():
    resp = code.get_one('yeti')
    assert resp == sample

def test_get_missint():
    resp = code.get_one('boxturtle')
    assert resp is None