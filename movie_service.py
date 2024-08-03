from database_manager import DatabaseManager
from movie import Movie


class MovieService:
    def __init__(self):
        self.db = DatabaseManager('movies.db')

    def create_table(self):
        self.db.create_table('movie_tb')

    def insert_data(self, movie: Movie):
        self.db.insert_data('movie_tb', {
            "id": None,
            "movie_code": movie.movie_code,
            "movie_title": movie.movie_title,
            "release_date": movie.release_date,
            "movie_url": movie.movie_url,
            "image_url": movie.image_url,
            "thumbnail_url": movie.thumbnail_url,
            "actor_name": movie.actor_name,
            "is_downloaded": int(movie.is_downloaded)
        })

    def get_movies(self):
        movies = self.db.get_all_movies('movie_tb')
        if movies is not None:
            return movies
        else:
            print("No movies found.")
            return []
    
    def get_movies_by_status(self, status: int = 0):
        movies = self.db.get_movie_by_downloaded_status('movie_tb', status)
        if movies is not None:
            return movies
        else:
            print("No movies found.")
            return []
        
    def update_movie_status(self, movie_code):
        self.db.update_movie_as_downloaded(movie_code)

    def close_connection(self):
        self.db.close_connection()
