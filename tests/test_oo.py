from oo.models.models import Movie, Program


def test_create_program():
    program = Program("the last dance", 2020)

    assert program.name == "the last dance".title()
    assert program.year == 2020


def test_add_likes_for_program():
    program = Program("training day", 2001)
    program.add_like()

    assert program.likes == 1


def test_create_film():
    film = Movie("the lord of the rings", 1986, 160)

    assert film.name == "the lord of the rings".title()
    assert film.year == 1986
    assert film.duration == 160


def test_add_likes_for_film():
    film = Movie("the lord of the rings", 1986, 160)
    film.add_like()

    assert film.likes == 1


def test_add_likes_for_film_when_is_not_zero():
    film = Movie("the lord of the rings", 1986, 160)
    film.add_like()

    assert film.likes != 0
