from models.models import Movie, Serie, Playlist

avengers = Movie("avengers - infinity war", 2018, 160)
rick_and_morty = Serie("rick and morty", 2016, 4)
lotr = Movie("the lord of the rings", 2000, 160)
adventure_time = Serie("adventure time", 2014, 8)

avengers.add_like()
avengers.add_like()
avengers.add_like()
lotr.add_like()
lotr.add_like()
rick_and_morty.add_like()
adventure_time.add_like()
adventure_time.add_like()

films_and_series = [avengers, rick_and_morty, lotr, adventure_time]
weekend_playlist = Playlist("weekend", films_and_series)
print(len(weekend_playlist))
print(avengers in weekend_playlist)
for program in weekend_playlist:
# É possível verificar o atributo dentro de um tipo de objeto em tempo de execução
    # A função hasattr verifica se um objeto tem determinado atributo
    # details = (
    #     program.duration if hasattr(program, "duration") else program.seasons
    # )
    print(program)



# O polimorfismo garante que classes filhas terão suas próprias especificidades
# e também terão as da superclasse
# Desvantagens da herança
# Algum método da classe herdada pode ter sido escrito em cpython e estar protegido
# Traz toda a complexidade da classe herdada, é necessário ler toda a sua documentação para essa implementação
