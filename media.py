import webbrowser


class Movie():

    """ This is done to create a Movie Library

    Attributes:
        title (str): the name of the movie.
        storyline (str): A brief description of the movie story.
        poster_image_url (str): URL of the oficial poster
        trailer_youtube_url (str): URL of a video with the movie trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
