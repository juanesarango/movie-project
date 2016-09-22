# README

This project aims to create a web page where visitors can review their movies and watch the trailers.
This project contains 3 files:

![Example View](https://cloud.githubusercontent.com/assets/7906289/18764760/800d0720-80d8-11e6-9bdf-42cc416d5732.png)

## Contains 

- `media.py` this is the module where the Movie() class is created.
- `fresh_tomatoes.py` here are the styles and scripts of the client side that is render in the browser.
- `entertaiment_server.py` is the script where the objects for each movie is created. And where the project is served.

## Usage

To run the project: 
```
run entertaiment_server.py
```

To add a movie edit this file and add a movie object to the movies array:

```
newMovie = media.Movie(title, 
                       storyline, 
                       poster_image_url, 
                       trailer_video_url)

movies.append(newMovie)
``` 

## Author
[Juan Esteban Arango] (https://github.com/juanesarango)

## License
MIT © [Juan Esteban Arango] (https://github.com/juanesarango)
