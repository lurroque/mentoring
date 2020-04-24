from oo.models.models import Film


def test_create_film():

    film = Film("the lord of the rings", 1986, 160)
    assert film.name == "the lord of the rings".title()
    assert film.year == 1986
    assert film.duration == 160
