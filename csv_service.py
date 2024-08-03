import csv
from movie import Movie


class CSVService:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        try:
            with open(self.file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                movies = []
                for row in reader:
                    movie = Movie(
                        id= 0,
                        movie_code=row['code'],
                        movie_title=row['title'],
                        release_date=row['releaseDate'],
                        movie_url=row['movieUrl'],
                        image_url=row['imageUrl'],
                        thumbnail_url=row['thumbNailUrl'],
                        actor_name=row['actorName'],
                        is_downloaded=False,
                    )
                    movies.append(movie)
                return movies
        except FileNotFoundError:
            print(f"Arquivo {self.file_path} não encontrado.")
            return []
