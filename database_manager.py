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
        CREATE TABLE IF NOT EXISTS {table_name}
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_code TEXT,
            movie_title TEXT,
            release_date TEXT,
            movie_url TEXT,
            image_url TEXT,
            thumbnail_url TEXT,
            actor_name TEXT,
            is_downloaded INTEGER DEFAULT 0
        );
    """

    try:
        self.conn.execute(query)
        print(f'Table {table_name} created!')
    except sqlite3.Error as e:
        print(f'Table creation failed with error: {e}')

def insert_movie(self, table_name: str, data: dict):
    query = f"""
        INSERT INTO {table_name} 
        (movie_code, movie_title, release_date, movie_url, image_url, thumbnail_url) 
        VALUES 
        ('{data['movie_code']}', '{data['movie_title']}', '{data['release_date']}', 
        '{data['movie_url']}', '{data['image_url']}', '{data['thumbnail_url']}', 
        '{data['actor_name']}', {int(data['is_downloaded'])});
        """
    
    try:
        self.conn.execute(query)
        print(f'Movie {data['movie_code']} inserted!')
    except sqlite3.Error as e:
        print(f'Movie insertion failed with error: {e}')

def get_all_movies(self, table_name: str):
    query = f"""SELECT * FROM {table_name};"""
    try:
        cursor = self.conn.execute(query)
        return [dict(row) for row in cursor]
    except sqlite3.Error as e:
        print(f'Movie retrieval failed with error: {e}')
        return None
    
def get_movie_by_downloaded_status(self, table_name, is_downloaded=0):
    query = f"""SELECT * FROM {table_name} WHERE is_downloaded={is_downloaded};"""
    
    try:
        cursor = self.conn.execute(query)
        return [dict(row) for row in cursor]
    except sqlite3.Error as e:
        print(f'Movie retrieval failed with error: {e}')
        return None
    
def close_connection(self):
    if self.conn is not None:
        self.conn.close()
        print('Connection closed!')
