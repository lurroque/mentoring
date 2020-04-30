class Program(object):
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def likes(self):
        return self._likes

    def add_like(self):
        self._likes += 1

    def __str__(self):
        return f"Name: {self._name}"\
                "- Year: {self.year}"\
                "- Likes: {self._likes}"


class Movie(Program):
    def __init__(self, name, year, duration):
        # A função super chama todos os métodos e atributos da classe mãe
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f"Name: {self._name}"\
                "- Year: {self.year}"\
                "- Duration: {self.duration}"\
                "- Likes: {self._likes}"


class Serie(Program):
    def __init__(self, name, year, seasons):
        # A função super chama todos os métodos e atributos da classe mãe
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f"Name: {self._name}"\
            "- Year: {self.year}"\
            "- Seasons: {self.seasons}"\
            "- Likes: {self._likes}"


class Playlist():
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    # Essa característica é chamada de composição
    # Duck typing é a característica da linguagem em herdar
    # comportamentos de outras classes
    # Evita acoplamento entre classes
    # Se algo for mudado na superclasse, algo pode quebrar na subclasse
    # Dunder method que permite que a classe seja um iterável
    # É possível verificar se um item está na lista. Ex: value in list
    def __geititem__(self, item):
        return self._programs[item]

    @property
    def size(self):
        return len(self._programs)

    @property
    def listing(self):
        return self._programs
