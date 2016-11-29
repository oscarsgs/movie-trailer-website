# MOVIE TRAILER WEBSITE

## Contents

- Introduction
- Files
- Usage
	- Adding movies
	- Displaying website


## Introduction

**Movie Trailer Website** is a small application created in *Python*, and it displays a number of movies with their information.

## Files

- `fresh_tomatoes.py`: Displays a website containing the poster, title and trailer of a number of movies.
- `fresher_tomatoes.py`: Displays a website containing the poster, title, storyline, rating and trailer for a number of movies.
- `entertainment_center.py`: Contains the movies to display and calls the module that will create the website
- `media.py`: Implements the class Movie

## Usage

### Adding movies

Open the `entertainment_center.py` file with an editor (Sublime Text or similar recommended).

A film consists of a title, a storyline, a poster image, a youtube trailer and a rating. Data should be introduced in an object from the class `Movie`.

Example:

```python
my_movie = media.Movie("Movie Name",
					   "Movie storyline",
					   "http://poster.image.url",
					   "youtube.com/MovieTrailerURL",
					   "U")
```

Valid movie ratings are: "U","PG","12","15" and "18". These can be edited from the `media.py` file.


### Displaying website

In the terminal/console type `python entertainment_center.py`. It will then create an *HTML file* displaying the movies and all their information.

By default, a website will be created using the `fresher_tomatoes.py` file. You can also use the `fresh_tomatoes.py` file instead by commenting this line
	
	`fresher_tomatoes.open_movies_page(movies)`

An uncommenting this line

	`#fresh_tomatoes.open_movies_page(movies)`

from the `entertainment_center.py` file.
 


