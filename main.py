from movie import Movie
from movie_service import MovieService
from csv_service import CSVService


class Main:
    def __init__(self):
        self.movie_service = MovieService()
        self.csv_service = CSVService('./csv_input/movies.csv')

    def main(self):
        # criar tabela e inserir dados manualmente
        self.movie_service.create_table()

        movies_csv = self.csv_service.read_csv()
        if movies_csv:
            for movie in movies_csv:
                self.movie_service.insert_data(movie)

        movies_list = self.movie_service.get_movies()
        for movie in movies_list:
            print(f"{movie}")

        self.movie_service.close_connection()

if __name__ == "__main__":
    main = Main()
    main.main()
