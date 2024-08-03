from movie import Movie
from movie_service import MovieService
from csv_service import CSVService
from txt_service import TXTService


class Main:
    def __init__(self):
        self.movie_service = MovieService()
        self.csv_service = CSVService('./input/movies.csv')
        self.txt_service = TXTService('./input/downloaded.txt')

    def main(self):
        self.movie_service.create_table()

        movies_csv = self.csv_service.read_csv()
        if movies_csv:
            for movie in movies_csv:
                self.movie_service.insert_data(movie)

        movies_list = self.movie_service.get_movies()
        for movie in movies_list:
            print(f"{movie}")

        self.movie_service.close_connection()

        print(self.txt_service.read_txt())

if __name__ == "__main__":
    main = Main()
    main.main()
