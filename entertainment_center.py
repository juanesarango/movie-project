import media
import fresh_tomatoes


movie1 = media.Movie('Inception',
                     'A thief, who steals corporate secrets through use of dream-sharing technology, '
                     'is given the inverse task of planting an idea into the mind of a CEO.',
                     'http://www.lashorasperdidas.com/wp-content/uploads//2010/08/critica-de-origen-cartel.jpg',  # NOQA
                     'https://www.youtube.com/watch?v=66TuSJo4dZM')

movie2 = media.Movie('The Dark Knight',
                     'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, '
                     'the caped crusader must come to terms with one of the greatest psychological tests '
                     'of his ability to fight injustice.',
                     'http://pics.filmaffinity.com/the_dark_knight-102763119-large.jpg',
                     'https://www.youtube.com/watch?v=EXeTwQWrcwY')

movie3 = media.Movie('Goal',
                     'The extremely talented Santiago Munez is given a chance at professional football, '
                     'after being spotted by a scout who has ties with Newcastle United.',
                     'http://www.gstatic.com/tv/thumb/movieposters/159369/p159369_p_v8_ab.jpg',
                     'https://www.youtube.com/watch?v=2UGIC8mrAoY')

movie4 = media.Movie('La vita e bella',
                     'When an open-minded Jewish librarian and his son become victims of the Holocaust, '
                     'he uses a perfect mixture of will, humor and imagination to protect his son from the '
                     'dangers around their camp.',
                     'http://ia.media-imdb.com/images/M/MV5BMTQwMTM2MjE4Ml5BMl5BanBnXkFtZTgwODQ2NTYxMTE@._V1_.jpg',
                     'https://www.youtube.com/watch?v=Tw33Xs4Q2r4')

movie5 = media.Movie('The Avengers',
                     "Earth's mightiest heroes must come together and learn to fight as a team if they are "
                     "to stop the mischievous Loki and his alien army from enslaving humanity.",
                     'http://2.bp.blogspot.com/-2erLGvxzM8E/VT0G1BxNlZI/AAAAAAAAT8A/ebVTGFgean8/s1600/Avengers_Age_of_Ultron_poster_usa.jpg',  # NOQA
                     'https://www.youtube.com/watch?v=eOrNdBpGMv8')

movies = [movie1, movie2, movie3, movie4, movie5]
fresh_tomatoes.open_movies_page(movies)
