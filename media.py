import webbrowser

class Movie():
	""" Defines methods and variables to store information about films 

		Attributes
		----------
		title: string
			Movie Title
		storyline: string
			The storyline or plot for the movie
		poster_image_url: string
			A link to a poster image for the movie
		trailer_youtube_url: string
			A link to youtube trailer video for the movie
		rating: string
			A rating for the movie. If the rating is not valid,
			"U" will be the rating.
	"""
	global VALID_RATINGS
	VALID_RATINGS = ["U","PG","12","15","18"]
	def __init__(self, movie_title,movie_storyline,poster_image,trailer_youtube,movie_rating):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		if movie_rating not in VALID_RATINGS:
			movie_rating = "U"
		self.rating = movie_rating
	""" Displays website """
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
