import media
import fresher_tomatoes
import fresh_tomatoes

clockwork_orange = media.Movie("A Clockwork Orange",
                               "In future Britain, Alex DeLarge, a charismatic \
                                and psycopath delinquent, who likes to \
                                practice crimes and ultra-violence with his \
                                gang, is jailed and volunteers for an \
                                experimental aversion therapy developed by \
                                the government in an effort to solve \
                                society's crime problem - but not all goes \
                                according to plan.",
                            "https://upload.wikimedia.org/wikipedia/en/4/48/Clockwork_orangeA.jpg",  # noqa
                            "https://www.youtube.com/watch?v=vN-1Mup0UI0",
                            "18")

shining = media.Movie("The Shining",
                                      "A family heads to an isolated hotel for the winter \
                      where an evil and spiritual presence influences the \
                      father into violence, while his psychic son sees \
                      horrific forebodings from the past and of the future.",
                      "https://upload.wikimedia.org/wikipedia/en/2/25/The_Shining_poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=6lClewZeGV0",
                      "15")

misery = media.Movie("Misery",
                     "After a famous author is rescued from a car crash by a \
                     fan of his novels, he comes to realize that the care he \
                     is receiving is only the beginning of a nightmare of \
                     captivity and abuse.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b4/Miseryposter.jpg",  # noqa
                     "https://www.youtube.com/watch?v=_axcdhxe_NU",
                     "18")

film_with_me_in_it = media.Movie("A Film With Me In It",
                                 "A broke, jobless actor and a broke, jobless \
                                 screenwriter set out to make a movie and \
                                 then find that life starts imitating art.",
                                 "https://upload.wikimedia.org/wikipedia/en/3/30/A_film_with_me_in_it.png",  # noqa
                                 "https://www.youtube.com/watch?v=1K-3Mu-sB6w",
                                 "13A")

star_wars = media.Movie("Star Wars: Episode IV",
                        "Luke Skywalker joins forces with a Jedi Knight, \
                        a cocky pilot, a wookiee and two droids to save the \
                        galaxy from the Empire's world-destroying \
                        battle-station, while also attempting to rescue \
                        Princess Leia from the evil Darth Vader.",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # noqa
                        "https://www.youtube.com/watch?v=vZ734NWnAHA",
                        "U")

meaning_of_life = media.Movie("Monty Python's The Meaning Of Life",
                              "The comedy team takes a look at life in all \
                              its stages in their own uniquely silly way.",
                              "https://upload.wikimedia.org/wikipedia/en/9/91/Meaningoflife.jpg",  # noqa
                              "https://www.youtube.com/watch?v=mVMzc5_rdGM",
                              "12")

movies = [clockwork_orange, shining, misery,
          film_with_me_in_it, star_wars, meaning_of_life]
# See fresher_tomatoes.py file for information
fresher_tomatoes.open_movies_page(movies)

# Normal execution
# fresh_tomatoes.open_movies_page(movies)
