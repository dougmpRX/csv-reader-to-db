from database_manager import DatabaseManager
from movie import Movie


class Main:
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

    def close_connection(self):
        self.db.close_connection()

    def main(self):
        self.create_table()

        movie = Movie(
            id=1,
            movie_code="M001",
            movie_title="Movie 1",
            release_date="2022-01-01",
            movie_url="https://www.movie.com/movie1",
            image_url="https://www.movie.com/image1.jpg",
            thumbnail_url="https://www.movie.com/thumbnail1.jpg",
            actor_name="Actor 1",
            is_downloaded=True
        )

        self.insert_data(movie)

        movies = self.get_movies()
        for movie in movies:
            print(f"{movie['id']} - {movie['movie_code']}")
            
        self.close_connection()

if __name__ == "__main__":
    main = Main()
    main.main()
