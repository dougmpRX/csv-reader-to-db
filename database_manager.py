import sqlite3

class DatabaseManager:
    def __init__(self, db_name: str):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_name)
            print(f'Database connection to {db_name} established.')
        except Exception as e:
            print(f'Error while connecting to database: {e}')

    def create_table(self, table_name: str):
        query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_code TEXT NOT NULL,
            movie_title TEXT NOT NULL,
            release_date TEXT NOT NULL,
            movie_url TEXT NOT NULL,
            image_url TEXT NOT NULL,
            thumbnail_url TEXT NOT NULL,
            actor_name TEXT NOT NULL,
            is_downloaded INTEGER NOT NULL
        );
        """
        try:
            self.conn.execute(query)
            print(f'Table {table_name} created!')
        except sqlite3.Error as e:
            print(f'Table creation failed with error: {e}')

    def insert_data(self, table_name: str, data: dict):
        query = f"""
        INSERT INTO {table_name} (movie_code, movie_title, release_date, movie_url, image_url, thumbnail_url, actor_name, is_downloaded)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        try:
            self.conn.execute(query, (data['movie_code'], data['movie_title'], data['release_date'], data['movie_url'], data['image_url'], data['thumbnail_url'], data['actor_name'], int(data['is_downloaded'])))
            self.conn.commit()
            print(f'Movie {data["movie_code"]} inserted!')
        except sqlite3.Error as e:
            print(f'Movie insertion failed with error: {e}')

    def get_all_movies(self, table_name: str):
        query = f"""SELECT * FROM {table_name};"""
        try:
            cursor = self.conn.execute(query)
            rows = cursor.fetchall()
            movies = []
            for row in rows:
                movie_dict = {}
                for i, col in enumerate(cursor.description):
                    movie_dict[col[0]] = row[i]
                movies.append(movie_dict)
            return movies
        except sqlite3.Error as e:
            print(f'Movie retrieval failed with error: {e}')
            return []

    def get_movie_by_downloaded_status(self, table_name, is_downloaded=0):
        query = f"""SELECT * FROM {table_name} WHERE is_downloaded=?;"""
        try:
            cursor = self.conn.execute(query, (is_downloaded,))
            rows = cursor.fetchall()
            movies = []
            for row in rows:
                movie_dict = {}
                for i, col in enumerate(cursor.description):
                    movie_dict[col[0]] = row[i]
                movies.append(movie_dict)
            return movies
        except sqlite3.Error as e:
            print(f'Movie retrieval failed with error: {e}')
            return []

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
            print('Connection closed!')
