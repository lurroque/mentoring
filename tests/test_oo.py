from oo.models.models import Film


def test_create_film():
    film = Film("the lord of the rings", 1986, 160)

    assert film.name == "the lord of the rings".title()
    assert film.year == 1986
    assert film.duration == 160

def test_add_likes_for_film():
    film = Film("the lord of the rings", 1986, 160)
    film.add_like()

    assert film.likes == 1

def test_add_likes_for_film_when_is_not_zero():
    film = Film("the lord of the rings", 1986, 160)
    film.add_like()

    assert film.likes != 0

