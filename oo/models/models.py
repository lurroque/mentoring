class Program(object):

    """Docstring for Program. """

    def __init__(self, name, year):
        """TODO: to be defined. """
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        """TODO: Docstring for name.
        :returns: TODO

        """
        return self._name

    @name.setter
    def name(self, new_name):
        """TODO: Docstring for name.

        """
        self._name = new_name

    @property
    def likes(self):
        """TODO: Docstring for likes.
        :returns: TODO

        """
        return self._likes

    def add_like(self):
        """TODO: Docstring for add_like.

        """
        self._likes += 1

    def __str__(self):
        """TODO: Docstring for show_attributes.
        :returns: TODO

        """
        return f"Name: {self._name} - Year: {self.year} - Likes: {self._likes}"


class Film(Program):

    """Docstring for Film. """

    def __init__(self, name, year, duration):
        """TODO: to be defined. """
        # A função super chama todos os métodos e atributos da classe mãe
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        """TODO: Docstring for show_attributes.
        :returns: TODO

        """
        return f"Name: {self._name} - Year: {self.year} - Duration: {self.duration} Likes: {self._likes}"


class Serie(Program):

    """Docstring for Serie. """

    def __init__(self, name, year, seasons):
        """TODO: to be defined. """
        # A função super chama todos os métodos e atributos da classe mãe
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        """TODO: Docstring for show_attributes.
        :returns: TODO

        """
        return f"Name: {self._name} - Year: {self.year} - Seasons: {self.seasons} Likes: {self._likes}"


class Playlist(list):

    """Docstring for PlayList. """

    def __init__(self, name, programs):
        """TODO: to be defined. """
        self.name = name
        self._programs = programs

    @property
    def size(self):
        """TODO: Docstring for size.
        :returns: TODO

        """
        return len(self._programs)

    @property
    def listing(self):
        """TODO: Docstring for listing.

        :returns: TODO

        """
        return self._programs
